import streamlit as st
from tabs import Tab_Noon_Overview, Tab_Noon_Github_Repo, Tab_Noon_Analysis

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Noon Orders Data Analysis Project",
    page_icon="📦",
)

# ---------- Header ----------
st.title("📦 Noon Orders Data Analysis")


# ----- Left menu -----
with st.sidebar:
    st.write("Analyzing the dataset of Noon e-commerce orders using SQL to extract meaningful insights about customer behavior, order volumes, product performance, and platform trends.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repository" , "📊 Results"])

# ---------- Overview Tab ----------
with tab1:
    Tab_Noon_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_Noon_Github_Repo.show()
    
# ---------- Results Tab ----------    
with tab3: 
    Tab_Noon_Analysis.show()
        