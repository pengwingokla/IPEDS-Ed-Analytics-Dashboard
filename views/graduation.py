import streamlit as st
import pandas as pd

from lib.utils import load_data, normalize_url

from components.viz.graduation.graphs import (
    plot_cohort_graduation_funnel,
    plot_cohort_graduation_line,
    plot_graduation_gender,
    plot_graduation_ethnicity,
    plot_graduation_statewide_comparison
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
    #########################################################
    # Statewide Comparison
    #########################################################
    st.markdown("### :orange[Graduation Statewide Comparison]")
    col5, col6, col7 = st.columns(3)

    # Set default state and institution
    DEFAULT_STATE = "New Jersey"
    DEFAULT_INSTITUTION = "New Jersey Institute of Technology"

    with col5:
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

    with col6:
        selected_institution = st.selectbox(
            label="Select an Institution",
            options=state_institutions,
            index=default_index
        )

    with col7:
        selected_year = st.selectbox(
            label="Select a Year",
            options=sorted(hf_custom["year"].unique(), reverse=True),
            index=0
        )

    col8, col9 = st.columns(2)
    with col8:
        fig = plot_graduation_statewide_comparison(hf_custom, selected_institution, selected_state, selected_year)
        st.plotly_chart(fig, use_container_width=True)