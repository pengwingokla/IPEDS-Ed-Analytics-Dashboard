import folium
import streamlit as st
from streamlit_folium import st_folium
import plotly.express as px

from lib.utils import load_data, normalize_url
from components.utils.load_img_url import load_header_image, SOURCE_URL
import components.utils.map_render as map_render

from components.viz.home.metrics import (
    grad_rate_metrics,
    admission_yield_metrics,
    selectivity_metrics
)

def show_home_page():
    # Load data
    try:
        hf_custom = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "custom.csv"))
        hf_adm = load_data(normalize_url("chloecodes/IPEDS_ADMISSION", "adm20-23.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("### :orange[New Jersey Institute of Technology Statistics]")
    with col2:
        admission_yield_metrics(hf_adm)
    with col3:
        selectivity_metrics(hf_adm)
    with col4:
        grad_rate_metrics(hf_custom)
    with col5:
        pass

    # Display about section
    with st.expander("About Dashboard"):
        st.write("This dashboard provides a comprehensive view of the University of New Jersey at Newark (NJIT).")

    col1, col2 = st.columns(2)
    with col1:
        # Load and display header image
        header_img = load_header_image(SOURCE_URL)
        if header_img:
            st.image(header_img, caption="Source: Yahoo Finance", use_container_width=True)
    with col2:
        # Create and display map
        njit_map = map_render.create_njit_map()
        st_data = st_folium(njit_map, width=600, height=470, use_container_width=True)
    
    