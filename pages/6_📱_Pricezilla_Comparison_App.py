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
    st.write("A barcode-based price comparison Android app designed to help users compare product prices.")
    st.write("###")
    st.write("**Author:** Ayman")


# ----- Title of the page -----
st.title("📱 Pricezilla – A Bar-code Based Price Comparison App")
st.divider()

