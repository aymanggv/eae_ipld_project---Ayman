import pandas as pd
# Some extra libraries for date conversions and build the webapp
import streamlit as st
import streamlit.components.v1 as components

from streamlit_pdf_viewer import pdf_viewer

# ----- Page configs -----
st.set_page_config(
    layout="wide",
    page_title="Pricezilla App",
    page_icon="📱",
)


# ----- Left menu -----
with st.sidebar:
    st.write("Tableau dashboard developed to present iGaming related insights.")
    st.write("###")
    st.write("**Author:** Ayman")


# ----- Title of the page -----
st.title("🎰 iGaming Analysis Dashboard")
st.divider()

st.header("Interactive Tableau View")

# st.markdown(
#     """
#     <style>
#     .iframe-container {
#         text-align: left;
#         margin-left: -212px;  /* Adjust this to move further to the left */
#     }
#     </style>
#     <div class="iframe-container">
#         <iframe src="https://app.powerbi.com/view?r=eyJrIjoiYjlmN2Y0NDgtNmUxZS00YTVmLWFmYzgtMzBjODlmYjhiYWZlIiwidCI6IjZmODM0MWEzLThlOWEtNDk0Mi04YWFmLTMxMWNhODExNjM4NCJ9" 
#         width="1140" height="542" style="border:none;" allowfullscreen="true" scrolling="yes"></iframe>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# components.iframe("https://public.tableau.com/views/Book1_17469997268340/PerformanceOverview?:showVizHome=no&:embed=true", 
#                 height=830,
#                 width=1500)

components.html(
    """
    <div style="transform: scale(0.65); transform-origin: top left; width: 2000px; height: 1100px; overflow: hidden;">
        <iframe src="https://public.tableau.com/views/Book1_17469997268340/PerformanceOverview?:showVizHome=no&:embed=true"
                width="1500" height="1000" style="border: none;">
        </iframe>
    </div>
    """,
    height=850,  # Adjust this to control the visible height in Streamlit
    scrolling=False
)


# st.divider()

# st.header("PDF View")

# pdf_viewer("data/Airport Analysis.pdf")