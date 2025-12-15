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
        valid_states = []
        for state in hf_custom["State"].dropna().unique():
            # Drop the 2-letters states indicating U.S. territories and freely associated states
            if len(state) > 2:
                valid_states.append(state)
        valid_states = sorted(valid_states)

        selected_state = st.selectbox(
            label="Select a State",
            # Drop the 2-letters states indicating U.S. territories and freely associated states
            options=valid_states,
            index=valid_states.index(DEFAULT_STATE)
        )

    # Filter institutions for selected state
    state_institutions = sorted(hf_custom[hf_custom['State'] == selected_state]["institution name"].unique())
    
    # Set default selection for institution multiselect
    default_selection = []
    if selected_state == DEFAULT_STATE and DEFAULT_INSTITUTION in state_institutions:
        default_selection = [DEFAULT_INSTITUTION]

    with col2:
        selected_institutions = st.multiselect(
            label="Select Institution(s)",
            options=state_institutions,
            default=default_selection
        )

    with col3:
        selected_year = st.selectbox(
            label="Select a Year",
            options=sorted(hf_custom["year"].unique(), reverse=True),
            index=0
        )

    col4, col5 = st.columns(2)
    with col4:
        fig = plot_ug_enrollment_statewide(hf_custom, selected_institutions, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col5:
        fig = plot_gr_enrollment_statewide(hf_custom, selected_institutions, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    
    col6, col7, col8 = st.columns(3)
    with col6:
        fig = plot_international_ug_statewide(hf_custom, selected_institutions, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col7:
        fig = plot_instate_ug_statewide(hf_custom, selected_institutions, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col8:
        fig = plot_outstate_ug_statewide(hf_custom, selected_institutions, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    

    fig = plot_women_ug_statewide(hf_custom, selected_institutions, selected_state, selected_year)
    st.plotly_chart(fig, use_container_width=True)