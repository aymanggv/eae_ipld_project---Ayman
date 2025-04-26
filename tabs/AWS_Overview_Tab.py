import streamlit as st
from PIL import Image

def show():
    st.header("📘 Project Overview")
    st.markdown(""" 
        # 🛒 Superstore Data Engineering Pipeline on AWS

    This project demonstrates an **end-to-end data engineering pipeline** on AWS using a **Superstore orders dataset**. It showcases how to ingest, partition, catalog, query, and visualize time-series retail data efficiently using AWS services like S3, Glue, Athena, and QuickSight.

    ---

    ## 🚀 Project Overview

    - **Goal**: Analyze daily Superstore orders using a scalable and cost-effective cloud pipeline.
    - **Dataset**: Retail order data, partitioned by date.
    - **Architecture**:  
    """)

    # Display the image using Streamlit's `st.image()`
    image = Image.open("data/super-store-end-to-end.png")
    st.image(image, caption="Data Architecture", use_container_width =True)

    st.markdown("""
        ## 🧰 Tech Stack

    | Tool               | Role                                          |
    |--------------------|-----------------------------------------------|
    | **AWS S3**         | Raw data storage (partitioned by snapshot date) |
    | **AWS Glue**       | Creates data catalog & schema from S3        |
    | **Amazon Athena**  | Serverless SQL querying engine                |
    | **Amazon QuickSight** | Business intelligence and dashboarding   |
    | **IAM**            | Access control for AWS services               |

    ---

    ## 📁 Folder Structure in S3

    - **Bucket Name**: `superstore`
    - **Main Folder**: `/orders`
    - **Partitioning**: `s3://superstore/orders/snapshot=01-04-2025/orders.csv` `s3://superstore/orders/snapshot=02-04-2025/orders.csv` ...
    
    > Partitioning the data by `snapshot` date improves **query performance** and **reduces cost** in Athena by scanning less data.

    ---

    ## 🔄 Pipeline Flow

    1. **Split Orders by Day**  
    Python script processes raw Superstore data and saves one file per day.

    2. **Upload to S3**  
    All daily files are uploaded to `s3://superstore/orders/` under respective `snapshot=` subfolders.

    3. **Catalog with AWS Glue**  
    - A Glue **crawler** is configured to scan the `orders` folder.
    - It automatically infers **schema**, **data types**, and **partitions**.
    - Results stored in the **AWS Glue Data Catalog**.

    4. **Query with Amazon Athena**  
    - Athena uses the Glue catalog to run **SQL queries** directly on S3 data.
    - Queries are efficient due to **partition pruning** based on snapshot.

    5. **Visualize with Amazon QuickSight**  
    - QuickSight connects to Athena as a data source.
    - Dashboards are created to explore KPIs like daily sales, top products, and customer trends.

    ---

    ## 🧠 Key Concepts Demonstrated

    - ✅ **Data Partitioning** for performance and cost-efficiency  
    - ✅ **Serverless querying** with Athena (no ETL needed)  
    - ✅ **Schema inference** with Glue  
    - ✅ **Cloud-native visualization** with QuickSight  
    - ✅ **End-to-end analytics** without provisioning servers

    ---

    ## 📈 Sample Use Cases

    - Identify daily or weekly sales trends.
    - Analyze top-selling products by region.
    - Monitor order volumes and revenue spikes.
    - Compare performance over different time snapshots.

    ---

    ## 📝 Next Steps & Improvements

    - Automate daily ingestion using **AWS Lambda** or **Step Functions**.
    - Add **data quality checks** with tools like **Great Expectations**.
    - Deploy **QuickSight dashboards** as reports with scheduled refresh.
    - Store original raw files in a `raw/` folder for traceability.

    ---

    ## 📂 Sample Athena Query

    ```sql
    SELECT snapshot, product_name, SUM(sales) AS total_sales
    FROM db_ayman_superstore.orders
    WHERE snapshot BETWEEN '2025-04-01' AND '2025-04-07'
    GROUP BY snapshot, product_name
    ORDER BY snapshot, total_sales DESC;
    ```

    """)

