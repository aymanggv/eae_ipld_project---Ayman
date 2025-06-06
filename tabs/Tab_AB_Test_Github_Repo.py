import streamlit as st

def show():
    st.header("📂 GitHub Repository")
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)
    
#     st.markdown(
#     """
#     <div style='text-align: center;'>
#         <h1 style='font-size: 50px;'>🚧 Under Construction 🚧</h1>
#         <p style='font-size: 20px;'>We're working hard to bring this feature to life.</p>
#         <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjdzZ250MTY1c3dwb2dlZXU1anBtOThkemE5eW5kaWQwMHExOXpmeSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cfGmVRsJI6wq6noGxP/giphy.gif" width="300" />
#     </div>
#     """,
#     unsafe_allow_html=True
# )

    

    st.markdown("""
        <style>
        .tree ul {
        list-style-type: none;
        font-family: monospace;
        padding-left: 1em;
        line-height: 1.6;
        }
        .tree input {
        display: none;
        }
        .tree label {
        cursor: pointer;
        }
        .tree input:checked + ul {
        display: block;
        }
        .tree ul ul {
        display: none;
        }
        .folder::before {
        content: "📁 ";
        }
        .file::before {
        content: "📄 ";
        }
        .comment {
        color: gray;
        font-size: 0.85em;
        font-style: italic;
        margin-left: 4px;
        }
        </style>

        <div class="tree">
        <ul>
        <li>
            <label class="folder" for="data">dataset</label>
            <input type="checkbox" id="data"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/AB-Testing/blob/main/dataset/ab_test_data.csv"> ab_test_data.csv </a> <span class="comment"># Dataset</span></li>
            </ul>
        </li>
        <li>
            <label class="folder" for="scripts">scripts</label>
            <input type="checkbox" id="scripts"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/AB-Testing/blob/main/scripts/ab_analysis.py"> ab_analysis.py </a> <span class="comment"># AB analysis practice</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/AB-Testing/blob/main/scripts/ab_analysis_case_study.ipynb"> ab_analysis_case_study.ipynb </a> <span class="comment"># Case study ipynb</span></li>
            <li class="file"> <a href="https://github.com/aymanggv/AB-Testing/blob/main/scripts/ab_generate_data.py"> ab_generate_data.py </a> <span class="comment"># Data generation script</span></li>
            </ul>
        </li>    
        </li>
        <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/LICENSE"> LICENSE </a> <span class="comment"># License info</span></li>
        <li class="file"> <a href="https://github.com/aymanggv/Ckara-Coffee-ETL-Data-Warehouse/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
