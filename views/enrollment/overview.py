import streamlit as st
import pandas as pd
from lib.utils import load_data, normalize_url

from components.viz.enrollment.enr_overview import (
    plot_ugenrollment_headcount,
    plot_ugenrollment_age_distribution,
    plot_ugenrollment_gender,
    plot_ugenrollment_ft_pt,
    plot_ugenrollment_race,
    plot_ugenrollment_residence
    )

from lib.text.helper import Help

def show_enrollment_overview_page():
    # Load data
    try:
        hf_custom = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "custom.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return
    
    selected_institution = st.selectbox(
        label="Select an Institution", 
        options=hf_custom["institution name"].unique(), 
        index=hf_custom["institution name"].unique().tolist().index("New Jersey Institute of Technology"))

    # Create columns for layout
    col1, col2 = st.columns(2)
    with col1:
        fig = plot_ugenrollment_headcount(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
        st.button("𝒾", help=Help.UG_ENROLLMENT_HEADCOUNT)
    with col2:
        fig = plot_ugenrollment_age_distribution(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        fig = plot_ugenrollment_gender(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = plot_ugenrollment_ft_pt(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    
    selected_year = st.selectbox(
        label="Select a Year",
        options=sorted(hf_custom[hf_custom['institution name'] == selected_institution]['year'].unique()),
        index=len(hf_custom[hf_custom['institution name'] == selected_institution]['year'].unique()) - 1
    )

    col5, col6 = st.columns(2)
    with col5:
        fig = plot_ugenrollment_race(hf_custom, selected_institution, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col6:
        fig = plot_ugenrollment_residence(hf_custom, selected_institution, selected_year)
        st.plotly_chart(fig, use_container_width=True)
