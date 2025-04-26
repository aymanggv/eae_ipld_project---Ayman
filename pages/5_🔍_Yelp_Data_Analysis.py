import streamlit as st
from tabs import Yelp_Overview_Tab, Yelp_Github_Repo_Tab, Yelp_Analysis_Tab

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Yelp Data Analysis Project",
    page_icon="🔍",
)

# ---------- Header ----------
st.title("🔍 Yelp Data Analysis Pipeline")


# ----- Left menu -----
with st.sidebar:
    st.write("Analyzing Yelp reviews using a scalable and cost-effective cloud pipeline.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 GitHub Repository" , "📊 Results"])

# ---------- Overview Tab ----------
with tab1:
    Yelp_Overview_Tab.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Yelp_Github_Repo_Tab.show()
    
# ---------- Results Tab ----------    
with tab3: 
    Yelp_Analysis_Tab.show()
        