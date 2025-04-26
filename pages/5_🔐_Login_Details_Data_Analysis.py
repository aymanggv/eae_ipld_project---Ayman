import streamlit as st
from tabs import Tab_Login_Overview, Tab_Login_Github_Repo, Tab_Login_Analysis

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Login Details Data Analysis Project",
    page_icon="🔐",
)

# ---------- Header ----------
st.title("🔐 Login Details Data Analysis")


# ----- Left menu -----
with st.sidebar:
    st.write("Analyzing the dataset of user login details using SQL to extract meaningful insights about user activity, platform usage, and more.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repository" , "📊 Results"])

# ---------- Overview Tab ----------
with tab1:
    Tab_Login_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_Login_Github_Repo.show()
    
# ---------- Results Tab ----------    
with tab3: 
    Tab_Login_Analysis.show()
        