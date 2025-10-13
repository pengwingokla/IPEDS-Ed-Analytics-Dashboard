import pandas as pd
import streamlit as st
from lib.utils import load_data, normalize_url
from lib.info_text import Help

from components.viz.admission.graphs import (
    plot_admission_yield,
    plot_admission_selectivity,
    plot_admission_headcount,
    )

def show_admission_page():
    # Load data
    try:
        hf_adm = load_data(normalize_url("chloecodes/IPEDS_ADMISSION", "adm20-23.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return
    
    selected_institution = st.selectbox(
        label="Select an Institution", 
        options=hf_adm["institution name"].unique(), 
        index=hf_adm["institution name"].unique().tolist().index("New Jersey Institute of Technology"))
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = plot_admission_yield(hf_adm, selected_institution)
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = plot_admission_selectivity(hf_adm, selected_institution)
        st.plotly_chart(fig2, use_container_width=True)
    
    fig3 = plot_admission_headcount(hf_adm, selected_institution)
    st.plotly_chart(fig3, use_container_width=True)