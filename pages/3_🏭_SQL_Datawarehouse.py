import streamlit as st
from pages import DWH_Overview_Tab_3_1, DWH_Github_Repo_Tab_3_2, DWH_EDA_Subtab_3_3, DWH_Advanced_Analytics_Subtab_3_4

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="SQL Data Warehouse Project",
    page_icon="🏭",
)

# ---------- Header ----------
st.title("🏭 SQL Data Warehouse and Data Engineering Project")


# ----- Left menu -----
with st.sidebar:
    st.write("From raw data to insights with clean folders, SQL pipelines (bronze/silver/gold), and solid docs.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repo", "📊 Results / Visuals"])

# ---------- Overview Tab ----------
with tab1:
    DWH_Overview_Tab_3_1.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    DWH_Github_Repo_Tab_3_2.show()
        

# ---------- Results Tab ----------
with tab3:
    
    # Nested tabs inside the main tab
    subtab1, subtab2 = st.tabs(["🔍 Exploratory Data Analysis", "📈 Advanced Analysis"])

    with subtab1:
        DWH_EDA_Subtab_3_3.show()
        

    with subtab2:
        DWH_Advanced_Analytics_Subtab_3_4.show()