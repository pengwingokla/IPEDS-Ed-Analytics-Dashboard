import streamlit as st
import pandas as pd
import plotly.express as px

from charts_enrollment import (
    create_total_enrollment_bar_chart,
    create_gender_enrollment_bar_chart,
    create_full_vs_part_time_trend,
    create_admission_yield_rate_chart,
    plot_admission_funnel,
    create_njit_vs_others_pie
)

# 🔹 Load data with caching
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# 🔹 Side Bar
def sidebar_button(label, key):
    # Apply colored markdown to highlight the selected tab
    button_label = f"{label}"
    if st.sidebar.button(button_label, key=key):
        st.session_state.active_page = key

# 🔸🔸 Streamlit App Layout 🔸🔸
st.set_page_config(page_title="Enrollment Comparison", layout="wide")
st.title("University Insights")

# 🔹 Load admissions dataset
adms_fpath = "adm/NJ_admission_data.csv"
adms_data = load_data(adms_fpath)

effy_fpath = "effy/NJ_enrollment_data.csv"
effy_data = load_data(effy_fpath)


# Initialize session state to track selected tab
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# Sidebar UI
st.sidebar.markdown("## MAIN")    
sidebar_button("Enrollment", "Enrollment")

if st.session_state.active_page == "Enrollment":
    st.markdown("""### Enrollment Dashboard""")

    # Filter controls (inside tab)
    # # 🔹 Select years
    available_years = sorted(adms_data["year"].dropna().unique())
    selected_years = st.multiselect(
        "Select Years", available_years, default=available_years[-1:])

    # 🔹 Filter schools
    filtered_adms = adms_data[adms_data["year"].isin(selected_years)]
    all_schools = sorted(filtered_adms["university_name"].dropna().unique())
    default_schools = [
        school for school in all_schools if "New Jersey Institute of Technology" in school or "Rutgers University-Newark" in school]
    selected_schools = st.multiselect(
        "Select Schools", all_schools, default=default_schools)

    # 🔹 Display Charts
    col1, col2 = st.columns(2)

    with col1:
        # st.subheader("📊 Total Enrollment Comparison")
        st.plotly_chart(create_total_enrollment_bar_chart(
            adms_data, selected_schools, selected_years), use_container_width=True)
        st.markdown("""
                    > This bar chart displays the **total enrollment of first-time, degree/certificate-seeking undergraduate students** in Fall 2023 for the selected institutions.""")


    with col2:
        # st.subheader("📈 Enrollment by Gender (Men vs Women)")
        st.plotly_chart(create_gender_enrollment_bar_chart(
            adms_data, selected_schools, selected_years), use_container_width=True)
        st.markdown("""
    > **Total Enrollment** and **Enrollment by Gender** charts show student headcounts for selected schools in a given year. While additional gender categories were introduced in 2022–23, this chart displays only binary gender data (men/women).
    """)

    # st.subheader("📉 Admission and Yield Rates (Selected Schools)")
    st.plotly_chart(create_admission_yield_rate_chart(
        adms_data, selected_schools, selected_years), use_container_width=True)
    st.markdown("""
    > **Admission Rate**  is calculated as the number of students admitted divided by the total number of applicants.
    > **Yield Rate** is calculated as the number of students enrolled divided by the number of students admitted.
    > This chart compares the percentage of applicants admitted (admission rate) and the percentage of admitted students who enrolled (yield rate) across selected institutions. Rates are based on first-time, degree/certificate-seeking undergraduate applicants under non-open admissions policies.
    """)


    # st.subheader("📊 Full-Time vs Part-Time Enrollment Over Time")
    default_school = "New Jersey Institute of Technology"
    all_schools = sorted(adms_data["university_name"].dropna().unique())
    trend_school = st.selectbox("Select a School for Enrollment Trend",
                                all_schools, index=all_schools.index(default_school))
    st.plotly_chart(create_full_vs_part_time_trend(
        adms_data, trend_school), use_container_width=True)
    st.markdown("""
    > This chart compares **full-time** and **part-time** enrollment trends over the years.  
    > It shows commitment level shifts in how students engage with their education.
    """)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Admission Funnel")
        st.plotly_chart(plot_admission_funnel(
            adms_data, trend_school), use_container_width=True)
        st.markdown(f"""
        > The **Admission Funnel** visualizes the pipeline from **Applicants → Admitted → Enrolled**.  
        > This helps illustrate where drop-offs occur in the enrollment journey for _{trend_school}_.
        """)

    with col4:
        
        # st.subheader("NJIT vs Other NJ Schools Enrollment Share")
        # 🔹 Select year (single selection)
        selected_year = st.selectbox("Select a Year", available_years, index=len(available_years) - 1)
        st.plotly_chart(create_njit_vs_others_pie(
            adms_data, [selected_year]), use_container_width=True)
        st.markdown("""
        > This chart shows **NJIT's enrollment share** relative to **all other New Jersey institutions**, based on total enrolled students for the selected years.
        """)

sidebar_button("Admission", "Admission")

if st.session_state.active_page == "Admission":
    st.markdown("""### Admission Dashboard""")
