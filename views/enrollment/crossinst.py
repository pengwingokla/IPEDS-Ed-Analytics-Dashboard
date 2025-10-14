import streamlit as st
import pandas as pd
from lib.utils import load_data, normalize_url

from components.viz.enrollment.enr_crossinst import (
    plot_enrollment_cross_institution,
    plot_ugenrollment_age_distribution_cross_institution,
    plot_ugenrollment_residence_cross_institution
)

def show_enrollment_cross_institution_comparison_page():
    # Load data
    try:
        hf_custom = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "custom.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return
    
    selected_multiple_institutions = st.multiselect(
        label="Select Institutions",
        options=hf_custom["institution name"].unique(),
        default=["New Jersey Institute of Technology","Rutgers University-Newark","Rutgers University-New Brunswick"])
    selected_year = st.selectbox(
        label="Select a Year",
        options=sorted(hf_custom["year"].unique(), reverse=True),
        index=0
    )
    
    col1, col2 = st.columns(2)
    with col1:
        fig = plot_enrollment_cross_institution(hf_custom, selected_multiple_institutions, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig = plot_ugenrollment_age_distribution_cross_institution(hf_custom, selected_multiple_institutions, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    
    
    fig = plot_ugenrollment_residence_cross_institution(hf_custom, selected_multiple_institutions, selected_year)
    st.plotly_chart(fig, use_container_width=True)