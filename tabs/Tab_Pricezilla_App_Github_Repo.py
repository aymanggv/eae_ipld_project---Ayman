import streamlit as st

def show():
    st.header("📂 GitHub Repository")
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

    

    st.markdown("""
        > **Note:** Since the project is too large to fully display with clickable GitHub links here,  
        > I have attached a **ZIP file** of the entire project in this repository.  
        > The **folder structure** for the app is shown below for reference.
            
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
                <label class="folder" for="barcode_app">barcode_app</label>
                <input type="checkbox" id="barcode_app"/>
                <ul>
                    <li>
                        <label class="folder" for="src">src</label>
                        <input type="checkbox" id="src"/>
                        <ul>
                            <li>
                                <label class="folder" for="main">main</label>
                                <input type="checkbox" id="main"/>
                                <ul>
                                    <li>
                                        <label class="folder" for="java">java</label>
                                        <input type="checkbox" id="java"/>
                                        <ul>
                                            <li>
                                                <label class="folder" for="com">com</label>
                                                <input type="checkbox" id="com"/>
                                                <ul>
                                                    <li>
                                                        <label class="folder" for="pricezilla">pricezilla</label>
                                                        <input type="checkbox" id="pricezilla"/>
                                                        <ul>
                                                            <li class="file">MainActivity.java</a></li>
                                                            <li class="file">Product.java</a></li>
                                                            <li class="file">Details.java</a></li>
                                                            <li class="file">ProductUtil.java</a></li>
                                                            <li class="file">ProductBaseActivity.java</a></li>
                                                            <li class="file">ProductAdditionActivity.java</a></li>
                                                            <li class="file">ProductReaderActivity.java</a></li>
                                                            <li class="file">ProductDetails.java</a></li>
                                                            <li class="file">SplashActivity.java</a></li>
                                                        </ul>
                                                    </li>
                                                </ul>
                                            </li>
                                        </ul>
                                    </li>
                                    <li>
                                        <label class="folder" for="res">res</label>
                                        <input type="checkbox" id="res"/>
                                        <ul>
                                            <li>
                                                <label class="folder" for="layout">layout</label>
                                                <input type="checkbox" id="layout"/>
                                                <ul>
                                                    <li class="file">activity_main.xml</a></li>
                                                    <li class="file">product_addition.xml</a></li>
                                                    <li class="file">product_reader.xml</a></li>
                                                    <li class="file">product_details.xml</a></li>
                                                    <li class="file">splash_activity.xml</a></li>
                                                </ul>
                                            </li>
                                            <li class="folder">drawable <span class="comment"># images/icons</span></li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li class="file">build.gradle</a></li>
                </ul>
            </li>
            <li>
                <label class="folder" for="docs">docs</label>
                <input type="checkbox" id="docs"/>
                <ul>
                    <li class="file"><a href="https://github.com/aymanggv/barcode-price-comparison-app/blob/main/docs/Individual%20project%20report.docx">Individual project report.docx</a></li>
                    <li class="file"><a href="https://github.com/aymanggv/barcode-price-comparison-app/blob/main/docs/FYPppt.pptx">FYPppt.pptx</a></li>
                </ul>
            </li>
            <li class="folder">images</li>
            <li class="file"><a href="https://github.com/aymanggv/barcode-price-comparison-app/blob/main/LICENSE">LICENSE</a></li>
            <li class="file"><a href="https://github.com/aymanggv/barcode-price-comparison-app/blob/main/README.md">README.md</a></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
