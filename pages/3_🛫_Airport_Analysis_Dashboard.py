import pandas as pd
# Some extra libraries for date conversions and build the webapp
import streamlit as st

from streamlit_pdf_viewer import pdf_viewer

# ----- Page configs -----
st.set_page_config(
    page_title="Ayman's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.write("Power BI dashboard developed to present cancelled and delayed flights for airports across the USA for the year 2018.")


# ----- Title of the page -----
st.title("🛫 Airport Analysis Dashboard")
st.divider()

pdf_viewer("data/Airport Analysis.pdf")