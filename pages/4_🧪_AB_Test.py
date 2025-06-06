import streamlit as st
from tabs import Tab_AB_Test_Overview, Tab_AB_Test_Github_Repo

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="A/B Test Analysis",
    page_icon="🧪",
)

# ---------- Header ----------
st.title("🧪 A/B Test Analysis: Click-Through Rate on CTA Button")


# ----- Left menu -----
with st.sidebar:
    st.write("A case study on an A/B test designed to measure the impact of a change on user click behavior")
    st.write("###")
    st.write("**Author:** Ayman")


# ---------- Tabs ----------
tab1, tab2 = st.tabs(["📘 Overview", "📂 GitHub Repository"])

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 50px;'>🚧 Under Construction 🚧</h1>
        <p style='font-size: 20px;'>We're working hard to bring this feature to life.</p>
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjdzZ250MTY1c3dwb2dlZXU1anBtOThkemE5eW5kaWQwMHExOXpmeSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cfGmVRsJI6wq6noGxP/giphy.gif" width="300" />
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Overview Tab ----------
with tab1:
    Tab_AB_Test_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_AB_Test_Github_Repo.show()
        