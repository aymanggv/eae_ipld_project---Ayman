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
    st.write("Power BI dashboard created to display financial findings of Pepsi.")
    st.write("Data recieved from EAE Business School as part of project. The live report can be viewed using the link: https://app.powerbi.com/groups/me/reports/97d39d5a-95a5-45c4-924d-0bf47f151f63/ReportSection3fa583ff48685abe5c72?experience=power-bi")


# ----- Title of the page -----
st.title("💹 Pepsi Financial Dashboard")
st.divider()

pdf_viewer("data/Pepsi Financial Report.pdf")