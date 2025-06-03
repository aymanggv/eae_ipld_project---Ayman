import streamlit as st

def show():
    st.header("📂 GitHub Repository")
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)
    
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 50px;'>🚧 Under Construction 🚧</h1>
        <p style='font-size: 20px;'>We're working hard to bring this feature to life.</p>
        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjdzZ250MTY1c3dwb2dlZXU1anBtOThkemE5eW5kaWQwMHExOXpmeSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cfGmVRsJI6wq6noGxP/giphy.gif" width="300" />
    </div>
    """,
    unsafe_allow_html=True
)

    

    # st.markdown("""
    #     <style>
    #     .tree ul {
    #     list-style-type: none;
    #     font-family: monospace;
    #     padding-left: 1em;
    #     line-height: 1.6;
    #     }
    #     .tree input {
    #     display: none;
    #     }
    #     .tree label {
    #     cursor: pointer;
    #     }
    #     .tree input:checked + ul {
    #     display: block;
    #     }
    #     .tree ul ul {
    #     display: none;
    #     }
    #     .folder::before {
    #     content: "📁 ";
    #     }
    #     .file::before {
    #     content: "📄 ";
    #     }
    #     .comment {
    #     color: gray;
    #     font-size: 0.85em;
    #     font-style: italic;
    #     margin-left: 4px;
    #     }
    #     </style>

    #     <div class="tree">
    #     <ul>
    #     <li>
    #         <label class="folder" for="data">datasets</label>
    #         <input type="checkbox" id="data"/>
    #         <ul>
    #         <li>
    #             <label class="folder" for="dimension">dimension_tables</label>
    #             <input type="checkbox" id="dimension"/>
    #             <ul>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Browser_Dim.csv"> Browser_Dim.csv </a> <span class="comment"># Browser details</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Date_Dim.csv"> Date_Dim.csv </a> <span class="comment"># Date data</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Employees_Dim.csv"> Employees_Dim.csv </a> <span class="comment"># Employee details</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Insta_Captions_Hashatgs_Dim.csv"> Insta_Captions_Hashatgs_Dim.csv </a> <span class="comment"># Instagram captions and hashtags</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Insta_Metrics_Dim.csv"> Insta_Metrics_Dim.csv </a> <span class="comment"># Instagram metrics data</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Neighbourhoods_Dim.csv"> Neighbourhoods_Dim.csv </a> <span class="comment"># Neighbourhood details</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Online_Clicks_Dim.csv"> Online_Clicks_Dim.csv </a> <span class="comment"># Click data</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Products_Dim.csv"> Products_Dim.csv </a> <span class="comment"># Product details</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Stores_Dim.csv"> Stores_Dim.csv </a> <span class="comment"># Store details</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/dimension_tables/Transaction_Dim.csv"> Transaction_Dim.csv </a> <span class="comment"># Transaction data</span></li>
    #             </ul>
    #         </li>
    #         <li>
    #             <label class="folder" for="fact">fact_tables</label>
    #             <input type="checkbox" id="fact"/>
    #             <ul>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/fact_tables/Instagram_Fact_Table.csv"> Instagram_Fact_Table.csv </a> <span class="comment"># Instagram fact table</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/fact_tables/Online_Clicks_Fact_Table.csv"> Online_Clicks_Fact_Table.csv </a> <span class="comment"># Clicks fact table</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/fact_tables/Sales_Fact_Table.csv"> Sales_Fact_Table.csv </a> <span class="comment"># Sales fact table</span></li>                
    #             </ul>
    #         </li>
    #         <li>
    #             <label class="folder" for="raw">raw_data</label>
    #             <input type="checkbox" id="raw"/>
    #             <ul>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/raw_data/All_ViewingActivity.csv"> All_ViewingActivity.csv </a> <span class="comment"># Browser data</span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/raw_data/Coffee%20Shop%20Sales.xlsx">Coffee Shop Sales.xlsx </a> <span class="comment"># Sales data </span></li>
    #             <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/data/raw_data/Instagram_data.csv"> Instagram_data.csv </a> <span class="comment"># Instagram data</span></li>                
    #             </ul>
    #         </li>
    #         </ul>
    #     </li>
    #     <li>
    #         <label class="folder" for="docs">docs</label>
    #         <input type="checkbox" id="docs"/>
    #         <ul>
    #         <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/docs/super-store-end-to-end.png"> super-store-end-to-end.png </a> <span class="comment"># ETL pipeline</span></li>
    #         </ul>
    #     </li>
    #         </ul>
    #     </li>
    #     <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/LICENSE"> LICENSE </a> <span class="comment"># License info</span></li>
    #     <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
    #     </ul>
    #     </div>
    #     """, unsafe_allow_html=True)
