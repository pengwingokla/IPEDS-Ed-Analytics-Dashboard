import streamlit as st
import pandas as pd

from lib.utils import load_data, normalize_url

from components.viz.grad_trends import (
    plot_cohort_graduation_rates_over_time
    )

def show_graduation_page():
    """
    Display the graduation analytics page
    """
    st.markdown("### :orange[Graduation Analytics]")

    # Load data
    try:
        df = load_data(normalize_url("chloecodes/IPEDS_CUSTOM", "c20-23.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return
    
    col1, col2 = st.columns(2)
    with col1:
        # create selectbox for institution
        institutions = df["institution name"].unique()
        selected_institution = st.selectbox(
            label="Select an Institution", 
            options=institutions, 
            index=institutions.tolist().index("New Jersey Institute of Technology"))
        fig = plot_cohort_graduation_rates_over_time(df, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
