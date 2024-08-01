import streamlit as st
from streamlit_extras.let_it_rain import rain


def app():
    st.title("📲CONTACT")
    st.subheader("Get in touch with me 📧")
    contact_form = """
    <form action="https://formsubmit.co/adk.koyalrani@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)
    rain(emoji="✉️",
        font_size=30,
        falling_speed=2,
        animation_length="1",)
    
# Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")