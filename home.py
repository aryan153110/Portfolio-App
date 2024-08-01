import streamlit as st
from streamlit_extras.let_it_rain import rain

def app():
    st.title("🏠HOME")
    rain(emoji="⭐",
        font_size=30,
        falling_speed=2,
        animation_length="1",)
    
    st.header("Aryan Prasad")
    st.subheader("Class: 12")
    st.subheader("Stream: Science(PCM)")

    col1,col2=st.columns(2)
    with col1:
        st.image("aryan1.jpg")
        original_title = """<p style="font-family:sans serif; color:Black; font-size: 20px; text-align:left"><b>Aryan Prasad</b></p> """
        st.markdown(original_title, unsafe_allow_html=True)

    with col2:
        para="""
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <blockquote>
                <p><span style="color:#263238;font-family:Arial, Helvetica, sans-serif;font-size:18px;">
                <strong>To start with, i'am a very interesting fellow with a selfless attitude towards anyone whom i come across with. 
                I'am of a very friendly nature and love to be with people who aren't selfish. I'm ambitious and can do anything to achieve my aim. 
                I'm of a very competitive nature but love to find good in everything i see.
                </strong></span></p>
            </blockquote>
            """
        st.markdown(para, unsafe_allow_html=True)
