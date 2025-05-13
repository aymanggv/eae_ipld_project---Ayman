import streamlit as st
from tabs import Tab_Roller_Coaster_Overview, Tab_Roller_Coaster_Dataset, Tab_Roller_Coaster_Results

# ---------- Page Config ----------
st.set_page_config(
    layout="wide",
    page_title="Roller Coaster Data Analysis Project",
    page_icon="🎢",
)

# ---------- Header ----------
st.title("🎢 Roller Coaster Data Analysis")


# ----- Left menu -----
with st.sidebar:
    st.write("Analyzing the dataset global database of roller coasters using Python to uncover patterns related to their design, location, and other such metrics.")
    st.write("###")
    st.write("**Author:** Ayman")

# # ---------- Tabs ----------
tab1, tab2, tab3 = st.tabs(["📘 Overview", "📂 Dataset" , "📊 Results"])

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

# # ---------- Overview Tab ----------
# with tab1:
#     Tab_Roller_Coaster_Overview.show()

# # ---------- GitHub Repo Tab ----------
# with tab2:
#     Tab_Roller_Coaster_Dataset.show()
    
# # ---------- Results Tab ----------    
# with tab3: 
#     Tab_Roller_Coaster_Results.show()
        