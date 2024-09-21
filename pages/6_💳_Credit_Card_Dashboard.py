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
    st.write("Power BI dashboard developed to present credit card insights for company.")


# ----- Title of the page -----
st.title("💳 Credit Card Dashboard")
st.divider()

pdf_viewer("data/Credit_Card_Report.pdf")