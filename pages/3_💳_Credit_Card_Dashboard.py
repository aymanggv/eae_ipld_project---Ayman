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

st.header("Interactive Power BI View")

st.markdown(
    """
    <style>
    .iframe-container {
        text-align: left;
        margin-left: -212px;  /* Adjust this to move further to the left */
    }
    </style>
    <div class="iframe-container"> 
        <iframe src= "https://app.powerbi.com/reportEmbed?reportId=f6a2fc13-3add-4b51-9414-2981a927c99c&autoAuth=true&ctid=41147bbe-0cc8-476e-b0ba-0a8c4e71e031" 
        width="1140" height="542" style="border:none;" allowfullscreen="true" scrolling="yes"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.header("PDF View")

pdf_viewer("data/Credit_Card_Report.pdf")