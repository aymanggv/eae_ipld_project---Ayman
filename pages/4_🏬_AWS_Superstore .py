import streamlit as st
from tabs import Tab_AWS_Overview, Tab_AWS_Github_Repo

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Superstore Data Engineering Project",
    page_icon="🏬",
)

# ---------- Header ----------
st.title("🏬 Superstore Data Engineering Pipeline on AWS")


# ----- Left menu -----
with st.sidebar:
    st.write("Analyzing daily Superstore orders using a scalable and cost-effective cloud pipeline.")
    st.write("###")
    st.write("**Author:** Ayman")

# ---------- Tabs ----------
tab1, tab2 = st.tabs(["📘 Overview", "📂 GitHub Repository"])

# ---------- Overview Tab ----------
with tab1:
    Tab_AWS_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_AWS_Github_Repo.show()
        