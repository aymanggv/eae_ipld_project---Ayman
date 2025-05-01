import streamlit as st
import pandas as pd

def show():
    st.header("📂 Dataset")
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)

    @st.cache_data
    def load_data():
        st.write("First 1000 rows of the dataset")
        data_path = "data/2015_Street_Tree_Census_-_Tree_Data_20250412.csv"

        temps_df = pd.read_csv(data_path) 

        return temps_df  # a Pandas DataFrame

    tree_census = load_data()

    st.dataframe(tree_census.head(1000))  