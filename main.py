import base64
import streamlit as st
from streamlit_option_menu import option_menu
import about, contact, home
import folium

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(page_title="PORTFOLIO", page_icon='smiley', layout="wide")

img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/free-vector/vibrant-summer-ombre-background-vector_53876-105765.jpg");
background-size: 100%;
background-position: top left;
background-repeat: round;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://i.pngimg.me/thumb/f/720/comrawpixel6230467.jpg");
background-position: left; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
opacity: 0%
}}


</style>
"""
st.get_option("theme.secondaryBackgroundColor")
st.get_option("theme.textColor")
st.markdown(page_bg_img, unsafe_allow_html=True)
apps = {
    "Home": home.app,
    "About": about.app,
    "Contact": contact.app
}
with st.sidebar:
    
    app = option_menu(menu_title="CONTENTS",
                      options=list(apps.keys()),
                      icons=['house-fill', 'person-circle', 'mailbox open'],
                      menu_icon='chat-text-fill',
                      default_index=0,
                      styles={"container": {"padding": "5!important", "background-colour": "transparent"},
                              "icons": {"color": "white", "font-size": "20px"},
                              "nav-link": {"color": "white", "font-size": "20px", "text-align": "left",
                                           "margin": "0px", "--hover-color": "#74bcb8"},
                              "nav-link-selected": {"background-color": "#3f8488"},
                              "menu-title": {"color": "white"}})



apps[app]()
