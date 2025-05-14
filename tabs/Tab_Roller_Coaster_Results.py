import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
        data_path = "data/coaster_db.csv"
        temps_df = pd.read_csv(data_path, low_memory=False) 
        return temps_df 

def show():
        st.subheader("🔍 Data Analysis")
        st.write("Exploration of the Roller Coaster dataset using Python.")

        df = load_data()
        
        
        st.markdown("""
                        ---
                        ### Describing the dataset
                        """)
        df.describe()
        
        
        

        st.markdown("""
                        ---
                        ### Scatter plot of trees where the diameter > 50 inches
                        """)
        big_trees = tree_census_subset[tree_census_subset['tree_dbh'] > 50]
        fig = big_trees[['tree_id', 'tree_dbh']].plot(kind = 'scatter', x='tree_id', y = 'tree_dbh', figsize= (20,10))
        plt.tight_layout()
        st.pyplot(plt.gcf())
        
        
        
        st.markdown("""
                        ---
                        ### Count of total tree types
                        """)
        fig = pd.DataFrame(tree_census_subset['spc_latin'].value_counts()).plot(kind='bar', figsize= (20,10))
        plt.tight_layout()
        st.pyplot(plt.gcf())
        

        st.markdown("""
                        ---
                        ### Count of the stewards
                        """)
        st.write(tree_census_subset['steward'].value_counts())
        
        
        st.markdown("""
                        ---
                        ### Count of the health of the sidewalk next to the specific tree
                        """) 
        st.write(tree_census_subset['sidewalk'].value_counts())
        
        
        st.markdown("""
                        ---
                        ### Count of how the trees are lcoated in relation to the curb
                        """)
        st.write(tree_census_subset['curb_loc'].value_counts())    
        
        
        
        st.markdown("""
                        ---
                        ### Trees with status as "stump"
                        """)
        st.write(tree_census_subset[tree_census_subset['status']== 'Stump'])   
        
        
        st.markdown("""
                        ---
                        ### Trees with status as "dead"
                        """)
        st.write(tree_census_subset[tree_census_subset['status']== 'Dead'])
        
        
        
        st.markdown("""
                        ---
                        ### Count of trees with different problems
                        """)
        tree_problems = tree_census_subset[['root_stone',
        'root_grate', 'root_other', 'trunk_wire', 'trnk_light', 'trnk_other',
        'brch_light', 'brch_shoe', 'brch_other']]
        
        st.write(tree_problems.apply(pd.Series.value_counts))