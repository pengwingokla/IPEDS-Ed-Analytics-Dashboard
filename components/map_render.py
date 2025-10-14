import folium
import streamlit as st
from streamlit_folium import st_folium

def create_njit_map():
        NJIT_COORDINATES = [40.7424, -74.1784]
        m = folium.Map(location=NJIT_COORDINATES, zoom_start=17)
        folium.Marker(
            NJIT_COORDINATES,
            popup=folium.Popup("NJIT", parse_html=False),
        ).add_to(m)
        return m