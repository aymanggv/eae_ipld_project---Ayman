import streamlit as st
import base64
from st_social_media_links import SocialMediaIcons


    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Ayman's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.header("Data Analytics and Data Science Portfolio")
    st.write("###")
    st.write("**Author:** Ayman")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Ayman</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "profpic.jpeg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Ayman" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Masters Graduate in Big Data and Analytics (Business Intelligence)"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a recent Masters graduate in Big Data and Analytics (Business Intelligence) from EAE Business School, in partnership with Universitat Politècnica de Catalunya.

- 🛩️ Previously worked as an Onbase Developer Administrator in Dubai.

- 🤖 Aspiring Data Analyst/Business Intelligence Analyst with proficiency in Workflow Development, SQL, Python, Power BI and object-oriented programming, enabling the creation of customized applications tailored to client requirements. Additionally, expertise in web and mobile application development complements a comprehensive skill-set in Data Analysis. Eager to contribute technical expertise and unwavering commitment to quality to drive corporate success and elevate the company's standing in the IT landscape.

- ✉️ My Email: [aymanggv@hotmail.com](mailto:aymanggv@hotmail.com)

- 🏠 Barcelona, Spain
""")

social_media_links = [
    "https://www.linkedin.com/in/aymangundru/",
    "https://www.instagram.com/aymangundru?igshid=YzVkODRmOTdmMw%3D%3D&utm_source=qr",
    "https://github.com/aymanggv",
]

colors = [None, None, "White",]

social_media_icons = SocialMediaIcons(social_media_links, colors)

social_media_icons.render()


