import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Ayman's Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** Ayman")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Ayman</h1></div>""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "profpic.jpeg"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Pursuing my Maters in Big Data and Analytics"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a student currently pursuing my Masters in Big Data and Analytics from EAE Business School 

- 🛩️ Previously worked as an Onbase Developer Adminsitrator

- 🤖 Versatile developer with expertise in creating an Android app for efficient product comparison, a Burger Builder web app using React, and a movie search website with HTML/CSS. Experienced in hardware projects like a humidity scanner with an FPGA board. Skilled in enhancing online communication through a Chat web app with React and Node.

- 🏂 I love reading, playing any type of sport and travelling.

- 📫 How to reach me: [Email](aymanggv@hotmail.com)     [LinkedIn](https://www.linkedin.com/in/ayman-gundru-a516971b2/)     [Instagram](https://www.instagram.com/aymangundru?igshid=YzVkODRmOTdmMw%3D%3D&utm_source=qr)

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
