import streamlit as st
import pandas as pd
from lib.utils import load_data, normalize_url

from components.viz.enrollment.enr_statewide import (
    plot_ug_enrollment_statewide,
    plot_gr_enrollment_statewide,
    plot_international_ug_statewide,
    plot_instate_ug_statewide,
    plot_outstate_ug_statewide,
    plot_women_ug_statewide
    )

def show_enrollment_state_wide_trends_page():
    # Load data
    try:
        hf_custom = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "custom.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return

    col1, col2, col3 = st.columns(3)

    # Set default state and institution
    DEFAULT_STATE = "New Jersey"
    DEFAULT_INSTITUTION = "New Jersey Institute of Technology"


    with col1:
        # Create select box for state
        selected_state = st.selectbox(
            label="Select a State",
            # Drop the 2-letters states indicating U.S. territories and freely associated states
            options=sorted([state for state in hf_custom['State'].dropna().unique() if len(state) > 2]),
            index=sorted([state for state in hf_custom['State'].dropna().unique() if len(state) > 2]).index(DEFAULT_STATE)
        )

    # Filter institutions for selected state
    state_institutions = sorted(hf_custom[hf_custom['State'] == selected_state]["institution name"].unique())
    
    # Set default index for institution selectbox
    default_index = 0
    if selected_state == DEFAULT_STATE and DEFAULT_INSTITUTION in state_institutions:
        default_index = state_institutions.index(DEFAULT_INSTITUTION)

    with col2:
        selected_institution = st.selectbox(
            label="Select an Institution",
            options=state_institutions,
            index=default_index
        )

    with col3:
        selected_year = st.selectbox(
            label="Select a Year",
            options=sorted(hf_custom["year"].unique(), reverse=True),
            index=0
        )

    col4, col5 = st.columns(2)
    with col4:
        fig = plot_ug_enrollment_statewide(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col5:
        fig = plot_gr_enrollment_statewide(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    
    col6, col7, col8 = st.columns(3)
    with col6:
        fig = plot_international_ug_statewide(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col7:
        fig = plot_instate_ug_statewide(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col8:
        fig = plot_outstate_ug_statewide(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    

    fig = plot_women_ug_statewide(hf_custom, selected_institution, selected_state, selected_year)
    st.plotly_chart(fig, use_container_width=True)