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
    st.write("Power BI dashboard created to display the global football analysis of the season 2023/2024.")
    


# ----- Title of the page -----
st.title("⚽ Football 2023/2024 Dashboard")
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
        <iframe src="https://app.powerbi.com/view?r=eyJrIjoiNTJhNmRlZjctMWZiMS00NDI1LTg4MmItNjk5YjllMWM5ZWVkIiwidCI6IjZmODM0MWEzLThlOWEtNDk0Mi04YWFmLTMxMWNhODExNjM4NCJ9" 
        width="1140" height="542" style="border:none;" allowfullscreen="true" scrolling="yes"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

#https://app.powerbi.com/reportEmbed?reportId=6fd799c8-4a74-4206-967f-d07fc2e8d1d2&autoAuth=true&ctid=41147bbe-0cc8-476e-b0ba-0a8c4e71e031 -- old link when publish to web diddnt work


st.divider()

st.header("PDF View")

pdf_viewer("data/Football_Final.pdf")