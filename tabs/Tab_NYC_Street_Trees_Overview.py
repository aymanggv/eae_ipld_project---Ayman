import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
        ### 🌳 NYC Street Trees — Exploratory Data Analysis (EDA)

    This project dives into the 2015 NYC Street Tree Census to understand the condition, diversity, and distribution of street trees across New York City.

    We explore the relationship between tree health, stewardship, location, and more through data visualization and cleaning techniques.

    ---

    ### 📁 Dataset

    - **Source**: [NYC Open Data — 2015 Street Tree Census](https://data.cityofnewyork.us/)
    - **File used**: `2015_Street_Tree_Census_-_Tree_Data.csv`
    - **Key Columns**:
    - `tree_id`, `tree_dbh`, `stump_diam`, `status`, `health`, `spc_latin`
    - `sidewalk`, `steward`, `curb_loc`, and various root/trunk/branch problem indicators

    ---

    ### 🔧 EDA Process

    #### 1. Data Cleaning
    - Dropped irrelevant columns and focused on essential fields.
    - Checked for and addressed missing values.
    - Cleaned and imputed `health`, `sidewalk`, and other categorical columns where necessary.
    - Special handling of `Dead` and `Stump` trees.

    #### 2. Data Exploration
    - Visualized tree and stump diameters via histograms and scatter plots.
    - Identified outliers (e.g., trees with `tree_dbh` > 50 inches).
    - Aggregated species frequency and analyzed dominant species across the city.
    - Explored stewardship participation and sidewalk conditions.

    #### 3. Problem Areas
    - Assessed environmental problems via features like:
    - `root_stone`, `trunk_wire`, `brch_light`, and more.
    - Summarized how often each problem occurred.

    ---

    ### 📈 Visualizations

    - Tree & stump diameter histograms
    - Scatter plots of large trees
    - Bar charts of most common tree species
    - Value counts of stewardship, health, and condition

    ---

    ### ✅ Key Insights

    - Some trees have extremely large trunk diameters, indicating age or data entry anomalies.
    - Species distribution is skewed toward a few common species.
    - Health data is missing more often in trees that are stumps or dead.
    - Active stewardship might positively influence tree health.

    ---

    ### 🚧 Future Improvements

    - Add borough-level analysis
    - Correlate tree health with species and location
    - Map visualization using folium or geopandas
    - Predictive modeling for tree health or maintenance needs

    """)

