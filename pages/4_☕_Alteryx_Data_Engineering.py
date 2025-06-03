import streamlit as st
from tabs import Tab_Ckara_Overview, Tab_Ckara_Github_Repo

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="CKARA Coffee: Data Engineering Project",
    page_icon="☕",
)

# ---------- Header ----------
st.title("☕ CKARA Coffee: Data engineering using Alteryx")


# ----- Left menu -----
with st.sidebar:
    st.write("A data engineering project simulating a real-world business scenario for a specialty coffee brand operating in Spain.")
    st.write("###")
    st.write("**Author:** Ayman")


# ---------- Tabs ----------
tab1, tab2 = st.tabs(["📘 Overview", "📂 GitHub Repository"])

# st.markdown(
#     """
#     <div style='text-align: center;'>
#         <h1 style='font-size: 50px;'>🚧 Under Construction 🚧</h1>
#         <p style='font-size: 20px;'>We're working hard to bring this feature to life.</p>
#         <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjdzZ250MTY1c3dwb2dlZXU1anBtOThkemE5eW5kaWQwMHExOXpmeSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cfGmVRsJI6wq6noGxP/giphy.gif" width="300" />
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# ---------- Overview Tab ----------
with tab1:
    Tab_Ckara_Overview.show()

# ---------- GitHub Repo Tab ----------
with tab2:
    Tab_Ckara_Github_Repo.show()
        