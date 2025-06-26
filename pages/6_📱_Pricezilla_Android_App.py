import streamlit as st
from tabs import Tab_Pricezilla_App_Overview, Tab_Pricezilla_App_Github_Repo

# ----- Page configs -----
st.set_page_config(
    layout="wide",
    page_title="Pricezilla App",
    page_icon="📱",
)


# ----- Title of the page -----
st.title("📱 Pricezilla – A Barcode Price Comparison App")


# ----- Left menu -----
with st.sidebar:
    st.write("A barcode-based price comparison Android app designed to help users compare product prices.")
    st.write("###")
    st.write("**Author:** Ayman")


# ---------- Tabs ----------
tab1, tab2 = st.tabs(["📘 Overview", "📂 GitHub Repository"])

# ---------- Overview Tab ----------
with tab1:
    Tab_Pricezilla_App_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_Pricezilla_App_Github_Repo.show()
    
        