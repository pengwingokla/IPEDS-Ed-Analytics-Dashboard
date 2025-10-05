import streamlit as st
import pandas as pd

from lib.utils import load_data, normalize_url

from components.viz.grad_trends import (
    plot_cohort_graduation_funnel,
    plot_cohort_graduation_line,
    plot_graduation_gender,
    plot_graduation_ethnicity
    )

def show_graduation_page():
    """
    Display the graduation analytics page
    """
    st.markdown("### :orange[Graduation Analytics]")

    # Load data
    try:
        hf_custom = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "custom.csv"))
        hf_grad = load_data(normalize_url("chloecodes/IPEDS_GRADUATION", "graduation.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return

    # Selectbox for institution and year
    selected_institution = st.selectbox(
        label="Select an Institution", 
        options=hf_custom["institution name"].unique(), 
        index=hf_custom["institution name"].unique().tolist().index("New Jersey Institute of Technology"))
    
    selected_year = st.selectbox(
        label="Select Year",
        options=sorted(hf_custom["year"].unique(), reverse=True),
        index=0)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = plot_cohort_graduation_funnel(hf_grad, selected_institution, selected_year=selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = plot_cohort_graduation_line(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
        
    col3, col4 = st.columns(2)
    with col3:
        fig = plot_graduation_gender(hf_custom, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        fig = plot_graduation_ethnicity(hf_custom, selected_institution, selected_year)
        st.plotly_chart(fig, use_container_width=True)