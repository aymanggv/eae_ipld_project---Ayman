import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
    ### 🚀 Yelp Data Analysis
    This project is an end-to-end data analytics pipeline for analyzing Yelp reviews and businesses. It extracts large-scale JSON data, processes it using Python, stores it in Amazon S3, loads it into Snowflake, and performs sentiment analysis using SQL and UDFs. The final step is to analyze and visualize the data. The dataset can be found on [Yelp Open Dataset](https://business.yelp.com/data/resources/open-dataset/).

    ---

    ### 🧰 Tech Stack
    - **Python**: Data extraction, transformation, and upload to S3
    - **Amazon S3**: Cloud storage for JSON data
    - **Snowflake**: Data warehouse for storing and processing data
    - **SQL & UDFs**: Data transformation and sentiment analysis
    - **Jupyter Notebooks**: Splitting the Yelp file into multiple smaller files
    
    ---
    
    ### 🔄 Data Pipeline Flow

        """)

    # Display the image using Streamlit's `st.image()`
    image = Image.open("data/End to End Flow - Yelp.png")
    st.image(image, caption="Data Architecture", use_container_width =True)

    st.markdown("""  
    - **Extract & Process JSON**: Python extracts Yelp reviews and business details.  
    - **Upload to S3**: JSON data is uploaded to an S3 bucket.  
    - **Load into Snowflake**: Data is ingested into Snowflake tables.  
    - **Flatten JSON Data**: SQL queries process nested JSON structures.  
    - **Sentiment Analysis**: UDF analyzes review sentiment.  
    - **Data Analysis & Insights**: SQL queries provide insights.                  

    ---

    ### 📈 BI: Analytics & Reporting (Data Analysis)

    #### Objective
    Develop SQL-based analytics to deliver detailed insights into:
    - ✅ **Sentiment Analysis**
    - ✅ **Restaurant Performance**
    - ✅ **Category Trends**

    These insights empower stakeholders with key business metrics, enabling strategic decision-making.  
    """)

