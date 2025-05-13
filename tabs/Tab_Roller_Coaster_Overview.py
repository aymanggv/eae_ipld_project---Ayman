import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
        ### 🎢 Roller Coasters — Exploratory Data Analysis (EDA)

        This project analyzes a global database of roller coasters to uncover patterns related to their design, location, and thrill factors like speed, height, and g-force.

        ---

        ### 📁 Dataset

        - **Source**: A dataset of roller coasters (`coaster_db.csv`)
        - **Included Attributes**:
        - `coaster_name`, `location`, `manufacturer`, `year_introduced`
        - Physical features: `speed_mph`, `height_ft`, `Inversions_clean`, `Gforce_clean`
        - `latitude`, `longitude`, and `Type_Main`

        ---

        ### 🔧 EDA Process

        #### 1. Data Cleaning

        - Removed unused or redundant columns.
        - Converted `opening_date_clean` to datetime format.
        - Handled missing values and cleaned feature names.

        #### 2. Univariate Analysis

        - Examined key roller coaster features:
        - Distribution of speed, height, number of inversions, and g-force.
        - Popular years for new coaster introductions.
        - Common coaster types (`Type_Main`) and manufacturers.

        #### 3. Bivariate Analysis

        - Explored relationships between features:
        - Speed vs. height
        - G-force vs. number of inversions
        - Trends over time: are coasters getting faster or taller?

        #### 4. Insights by Location

        - Identified locations with the fastest roller coasters (filtered for places with at least 10 entries).
        - Analyzed geographic trends using latitude and longitude.

        ---

        ### 📈 Visualizations

        - Histograms and KDE plots for numeric features.
        - Scatter plots for height vs. speed, etc.
        - Bar charts for coaster types and manufacturers.
        - Time series plots for coaster construction trends.

        ---

        ### ✅ Key Insights

        - The fastest coasters are often located in major amusement parks in the U.S. and Japan.
        - A few manufacturers dominate the roller coaster industry.
        - There’s a visible trend toward taller, faster coasters over time.
        - More recent coasters tend to offer higher g-forces and more inversions.

        ---

        ### 🚀 Future Work

        - Add interactive visualizations with Plotly or Altair
        - Build a dashboard summarizing coaster stats by country
        - Cluster coasters by thrill factor using unsupervised learning

    """)

