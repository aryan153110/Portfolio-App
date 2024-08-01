import streamlit as st
from streamlit_extras.let_it_rain import rain
import folium
from streamlit_folium import st_folium
def app():
    st.title("ABOUT")
    rain(emoji="📝",
        font_size=30,
        falling_speed=2,
        animation_length="1",)
    col1,col2=st.columns(2)
    with col1:
        st.write("I live in Kalyani, Dist- Nadia, West Bengal, Pin-741235")
   
        m = folium.Map(location=[22.964883822523444, 88.42836908965704], zoom_start=13)
        folium.Marker(location=[22.965970454585744, 88.43254260680848], popup='Kalyani, Nadia').add_to(m)
        st_folium(m, height=500)

    
