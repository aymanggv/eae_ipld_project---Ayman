import streamlit as st

def show():
    st.header("📂 GitHub Repository")
    # st.markdown("""
    #     🔗[Click here to view the full project on GitHub](https://github.com/aymanggv/data-warehouse-project)

    #     _You can explore all code, datasets, and documentation there._  
    # """)

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
            <label class="folder" for="datasets">datasets</label>
            <input type="checkbox" id="datasets"/>
            <ul>
            <li>
                <label class="folder" for="partition">partitioned_data</label>
                <input type="checkbox" id="partition"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/dataset/partitioned_data/orders_1.txt"> orders_1.txt </a> <span class="comment"># Partitioned orders data</span></li>
                <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/dataset/partitioned_data/orders_2.txt"> orders_2.txt </a> <span class="comment"># Partitioned orders data</span></li>
                </ul>
            </li>
            <li>
                <label class="folder" for="raw">raw_data</label>
                <input type="checkbox" id="raw"/>
                <ul>
                <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/dataset/raw_data/Sample%20-%20Superstore.csv"> Sample - Superstore.csv </a> <span class="comment"># Raw orders data</span></li>
                </ul>
            </li>
            </ul>
        </li>
        <li>
            <label class="folder" for="docs">docs</label>
            <input type="checkbox" id="docs"/>
            <ul>
            <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/docs/super-store-end-to-end.png"> super-store-end-to-end.png </a> <span class="comment"># ETL pipeline</span></li>
            </ul>
        </li>
            </ul>
        </li>
        <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/LICENSE"> LICENSE </a> <span class="comment"># License info</span></li>
        <li class="file"> <a href="https://github.com/aymanggv/Superstore-Data-Engineering/blob/main/README.md"> README.md </a> <span class="comment"># Project overview</span></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
