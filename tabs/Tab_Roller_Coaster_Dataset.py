import streamlit as st
import pandas as pd

def show():
    st.header("📂 Dataset")
    st.markdown("""
                ##### Roller Coaster Dataset. 
                ---
                """)
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)

    @st.cache_data
    def load_data():
        data_path = "data/coaster_db.csv"

        temps_df = pd.read_csv(data_path, low_memory=False) 

        return temps_df  # a Pandas DataFrame

    df = load_data()

    st.dataframe(df.head(1000))  