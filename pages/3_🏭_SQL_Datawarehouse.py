import streamlit as st
from tabs import Tab_DWH_Overview_3_1, Tab_DWH_Github_Repo_3_2, Tab_DWH_EDA_3_3, Tab_DWH_Advanced_Analytics_3_4

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
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repository", "📊 Results"])

# ---------- Overview Tab ----------
with tab1:
    Tab_DWH_Overview_3_1.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_DWH_Github_Repo_3_2.show()
        

# ---------- Results Tab ----------
with tab3:
    
    # Nested tabs inside the main tab
    subtab1, subtab2 = st.tabs(["🔍 Exploratory Data Analysis", "📈 Advanced Analysis"])

    with subtab1:
        Tab_DWH_EDA_3_3.show()
        

    with subtab2:
        Tab_DWH_Advanced_Analytics_3_4.show()