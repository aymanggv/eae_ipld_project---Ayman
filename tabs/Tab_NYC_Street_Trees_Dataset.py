import streamlit as st
import pandas as pd

def show():
    st.header("📂 Dataset")
    st.markdown("""
                ##### ⚠️ Note: The original dataset has been reduced in size due to file size limitations on GitHub. This version includes a representative sample for analysis purposes. 
                ---
                """)
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)

    @st.cache_data
    def load_data():
        st.write("First 1000 rows of the dataset")
        data_path = "data/2015_Street_Tree_Census_-_Tree_Data_20250412.csv"

        temps_df = pd.read_csv(data_path, low_memory=False) 

        return temps_df  # a Pandas DataFrame

    tree_census = load_data()

    st.dataframe(tree_census.head(1000))  