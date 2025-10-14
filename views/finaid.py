import streamlit as st
import pandas as pd

from lib.utils import load_data, normalize_url
from lib.text.helper import Help

from components.viz.finaid.graphs import (
    plot_tuition_type_pie,
    plot_aid_type_stackedbar,
    plot_aid_received_linechart,
    plot_category_aid_disbursed,
    plot_total_aid_disbursed,
    plot_total_aid_disbursed_linechart,
    plot_student_loan_dualaxis,
    plot_student_loan_percentages
    )

def show_financial_aid_page():
    # Load data
    try:
        hf_finaid = load_data(normalize_url("chloecodes/IPEDS_SFA", "sfa.csv"))
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return

    st.markdown("""### :orange[Overview]""")

    # Selectbox for institution and year
    selected_institution = st.selectbox(
        label="Select an Institution", 
        options=hf_finaid["institution name"].unique(), 
        index=hf_finaid["institution name"].unique().tolist().index("New Jersey Institute of Technology"))
    
    # col1, col2 = st.columns(2)
    st.button("𝒾", help=Help.AID_TYPE_COMPOSITION)
    fig = plot_aid_type_stackedbar(hf_finaid, selected_institution)
    st.plotly_chart(fig, use_container_width=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.button("𝒾", help=Help.TOT_AMT_AID_COMPOSITION)
        fig = plot_total_aid_disbursed_linechart(hf_finaid, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.button("𝒾", help=Help.GENERAL_AID_TYPE_COMPOSITION)
        fig = plot_aid_received_linechart(hf_finaid, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""### :orange[Student Loan Analysis]""")
    col5, col6 = st.columns(2)
    # with col5:
    #     fig = plot_student_loan_dualaxis(hf_finaid, selected_institution)
    #     st.plotly_chart(fig, use_container_width=True)
    
    with col5:
        fig = plot_student_loan_percentages(hf_finaid, selected_institution)
        st.plotly_chart(fig, use_container_width=True)
    

    st.markdown("""### :orange[Analysis For Selected Year]""")

    selected_year = st.selectbox(
        label="Select Year",
        options=sorted(hf_finaid["year"].unique(), reverse=True),
        index=0)
    col10, col11 = st.columns(2)

    with col10:
        fig = plot_tuition_type_pie(hf_finaid, selected_institution, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    with col11:
        fig = plot_category_aid_disbursed(hf_finaid, selected_institution, selected_year)
        st.plotly_chart(fig, use_container_width=True)
    
    plot_total_aid_disbursed(hf_finaid, selected_institution, selected_year)