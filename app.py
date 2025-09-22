import streamlit as st
import pandas as pd
import plotly.express as px
from docs.info_button_text import (
    get_enrollment_donut_chart_help,
    get_enrollment_trends_help,
    get_full_vs_part_time_trend_help,
    get_admission_funnel_help,
    get_total_enrollment_help,
    get_gender_enrollment_help,
    get_admission_yield_rate_help,
    get_graduation_funnel_help,
    get_top20_institutions_aid_help,
    get_net_price_by_income_help,
    get_aid_type_breakdown_help,
)

from plot_functions.charts_enrollment import (
    plot_enrollment_over_years,
    create_total_enrollment_bar_chart,
    create_gender_enrollment_bar_chart,
    create_full_vs_part_time_trend,
    create_full_vs_part_time_trend_multiple,
    create_admission_yield_rate_chart,
    plot_admission_funnel,
    create_njit_vs_others_pie,
    plot_njit_share_change,
)

from plot_functions.charts_graduation import (
    plot_graduation_funnel,
    plot_graduation_by_race_treemap,
    # plot_graduation_by_gender_bar,
    plot_university_wide_graduation_rate,
    plot_school_graduation_share_pie,
    plot_school_graduation_share_pie_by_unitid
)

from plot_functions.charts_finaid import (
    plot_net_price_by_income,
    plot_top20_institutions_by_total_aid,
    plot_aid_type_breakdown_percent
)

# ---- Set Page Config ----
st.set_page_config(
    page_title="University Insights",
    page_icon="img/njit_logo.jpg",  # Make sure this path exists in the repo
    layout="wide"
)

# ---- Custom CSS for Sidebar Buttons ----
st.markdown("""
    <style>
        .sidebar-button button {
            width: 100% !important;
            text-align: left !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Load Data with Caching ----
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# ---- Sidebar Navigation ----
st.sidebar.markdown("## 📚 Navigation")

# Initialize session states
if "active_page" not in st.session_state:
    st.session_state.active_page = "Enrollment"
if "enrollment_section" not in st.session_state:
    st.session_state.enrollment_section = None

# ---- High-level Navigation Buttons ----
with st.sidebar:
    st.markdown('<div class="sidebar-button">', unsafe_allow_html=True)
    if st.button("Enrollment"):
        st.session_state.active_page = "Enrollment"
    if st.button("Graduation"):
        st.session_state.active_page = "Graduation"
    if st.button("Financial Aid"):
        st.session_state.active_page = "Financial Aid"
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Sub-Section Buttons for Enrollment ----
if st.session_state.active_page == "Enrollment":
    st.sidebar.markdown("### Enrollment Sections")
    with st.sidebar:
        st.markdown('<div class="sidebar-button">', unsafe_allow_html=True)
        if st.button("NJIT’s Position in Statewide Trends"):
            st.session_state.enrollment_section = "section1"
        if st.button("Insights for Selected Institution"):
            st.session_state.enrollment_section = "section2"
        if st.button("Comparison Across Institutions"):
            st.session_state.enrollment_section = "section3"
        st.markdown('</div>', unsafe_allow_html=True)

# 🔹 Page Config
# ---- Main Title ----
st.title("Institutional Analytics")

# ---- Default Welcome Page ----
if (
    st.session_state.active_page == "Enrollment" and 
    st.session_state.enrollment_section is None
):
    st.markdown("# 👋")
    st.markdown("### Welcome to a Comprehensive View of :red[NJIT]’s Performance")
    st.markdown("""
        This dashboard provides insights into institutional trends for NJIT and its 
        peer universities across New Jersey. Use the navigation menu on the left to explore:
        
        - **Statewide Enrollment Trends**
        - **Institution-Specific Enrollment & Admission**
        - **Multi-Institution Comparisons**
        
        Start by choosing a section from the sidebar.
    """)

# 🔹 Load datasets
adms_fpath = "data/NJ_admission_data.csv"
effy_fpath = "data/NJ_enrollment_data.csv"
sfa_fpath = "data/NJ_sfa_data.csv"
enrollment_dbt_path = "dbt-processed/enrollment.csv"
adms_data = load_data(adms_fpath)
effy_data = load_data(effy_fpath)
sfa_data = load_data(sfa_fpath)
enrollment_data_dbt = load_data(enrollment_dbt_path)

# 🔸🔸 Enrollment Page 🔸🔸
if st.session_state.active_page == "Enrollment":
    if st.session_state.enrollment_section == "section1":
        st.markdown("""### :orange[NJIT’s Position in Statewide Enrollment Trends]""")
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        with col1:
            # First, render the chart first with a placeholder year
            chart_placeholder = st.empty()
            st.button("𝒾", help=get_enrollment_donut_chart_help())

            # Then render dropdown below the chart
            available_years = sorted(adms_data["year"].dropna().unique())
            selected_year = st.selectbox("Select a Year", available_years, index=len(available_years) - 1, key="year_selector_pie")

            # Now render chart based on actual user-selected year
            chart_placeholder.plotly_chart(create_njit_vs_others_pie(adms_data, [selected_year]), use_container_width=True)
        with col2:
            st.plotly_chart(plot_njit_share_change(adms_data), use_container_width=True)
            st.button("𝒾", help="This bar chart illustrates undergraduate enrollment trends over time, comparing the selected institution's enrollment to that of all other NJ schools. It also shows the annual change in the selected institution’s share of total enrollment compared to the year before it to evaluate relative growth or decline over multiple years.")
        with col3:
            st.plotly_chart(plot_enrollment_over_years(enrollment_data_dbt), use_container_width=True)
            st.button("𝒾", help="This line chart shows the total enrollment trend over time for the selected institution. It provides a historical view of how enrollment has changed across all available years in the dataset.")

    elif st.session_state.enrollment_section == "section2":
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""### :orange[Enrollment and Admissions Insights for Selected Institution]""")

        
        col1, col2 = st.columns(2)
        with col1:
            default_school = "New Jersey Institute of Technology"
            all_schools = sorted(adms_data["university_name"].dropna().unique())
            trend_school = st.selectbox("Select a School for Enrollment Trend",
                                        all_schools, index=all_schools.index(default_school))
        with col2:
            available_years = sorted(adms_data["year"].dropna().unique())
            selected_year = st.selectbox("Select a Year", available_years, index=len(available_years) - 1)

        col3, col4 = st.columns(2)
        with col3:
            st.plotly_chart(create_full_vs_part_time_trend(adms_data, trend_school), use_container_width=True)
            st.button("𝒾", help=get_full_vs_part_time_trend_help())

        with col4:
            st.plotly_chart(plot_admission_funnel(adms_data, trend_school, selected_year=selected_year), use_container_width=True)
            st.button("𝒾", help="This funnel chart illustrates the admissions pipeline for a selected institution and year. It breaks down the total number of applicants, how many were admitted, and how many ultimately enrolled, providing a clear view of conversion at each stage of the enrollment process.")

    elif st.session_state.enrollment_section == "section3":
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""### :orange[Undergraduate Enrollment Comparison Across Institutions]""")

        col1, col2 = st.columns([1, 3])
        with col1:
            available_years = sorted(adms_data["year"].dropna().unique())
            selected_years = st.multiselect(
                "Select Years", available_years, default=available_years[-1:])

        with col2:
            filtered_adms = adms_data[adms_data["year"].isin(selected_years)]
            all_schools = sorted(filtered_adms["university_name"].dropna().unique())
            default_schools = [
                school for school in all_schools if "New Jersey Institute of Technology" in school or "Rutgers University-Newark" in school
            ]
            selected_schools = st.multiselect(
                "Select Schools", all_schools, default=default_schools)

        if selected_years and selected_schools:
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(create_total_enrollment_bar_chart(adms_data, selected_schools, selected_years), use_container_width=True)
                st.button("𝒾", help=get_total_enrollment_help())
            with col2:
                st.plotly_chart(create_gender_enrollment_bar_chart(adms_data, selected_schools, selected_years), use_container_width=True)
                st.button("𝒾", help="Enrollment by gender for selected institutions.")
            st.plotly_chart(create_admission_yield_rate_chart(adms_data, selected_schools, selected_years), use_container_width=True)
            st.button("𝒾", help="This grouped bar chart compares the admission rate and yield rate across selected institutions for a specific year. Admission rate represents the percentage of applicants who were admitted, while yield rate indicates the percentage of admitted students who chose to enroll. This visualization helps assess the selectivity and enrollment effectiveness of different institutions.")
            st.plotly_chart(create_full_vs_part_time_trend_multiple(adms_data, selected_schools), use_container_width=True)
        else:
            st.warning("Please select at least one school and one year to view the charts.")


# 🔸🔸 Graduation Page 🔸🔸
elif st.session_state.active_page == "Graduation":

    st.markdown("""### :orange[Graduation]""")
    grad_fpath = "data/NJ_graduation_data.csv"
    grad_data = load_data(grad_fpath)
    grad_data_dbt_fpath = "dbt-processed/graduation.csv"
    grad_data_dbt = load_data(grad_data_dbt_fpath)

    # Get all schools first
    all_schools = sorted(grad_data["university_name"].dropna().unique())
    
    if all_schools:
        default_schools = [
            school for school in all_schools if "New Jersey Institute of Technology" in school or "Rutgers University-Newark" in school
        ]
        selected_school = st.selectbox("Select a School", all_schools, index=all_schools.index(default_schools[0]))
        selected_unitid = grad_data[grad_data["university_name"] == selected_school]["unitid"].iloc[0]
        
        # Filter years based on selected school
        school_data = grad_data[grad_data["university_name"] == selected_school]
        available_years = sorted(school_data["year"].dropna().unique())
        col1, col2 = st.columns(2)
        with col1:
            selected_years = [st.selectbox(
                "Select Year", available_years, index=len(available_years)-1)]

        if selected_years:

            col1, col2 = st.columns(2)
            with col1:
                # Graduation Outcomes of Bachelor’s Cohort (4-Year Institutions)
                fig = plot_graduation_funnel(grad_data_dbt, selected_institution_id=selected_unitid, selected_year=selected_years[-1])
                # fig = graduation_funnel_chart(grad_data, selected_unitid=selected_unitid, selected_year=selected_years[-1])
                st.plotly_chart(fig, use_container_width=True)
                st.button("𝒾", help=get_graduation_funnel_help())
            with col2:
                # fig = plot_graduation_rate_trend(grad_data, selected_unitid=selected_unitid)
                fig = plot_university_wide_graduation_rate(grad_data_dbt, selected_unitid=selected_unitid)
                st.plotly_chart(fig, use_container_width=True)

            col3, col4 = st.columns(2)
            with col3:
                selected_year = st.selectbox("Select a Year", available_years, index=len(available_years) - 1, key="grad_year_for_pie")
            with col4:
                selected_school_for_pie = st.selectbox("Select a School for Comparison", all_schools, index=all_schools.index(selected_school), key="grad_school_for_pie")
                selected_unitid_for_pie = grad_data[grad_data["university_name"] == selected_school_for_pie]["unitid"].iloc[0]
            col5, col6 = st.columns(2)
            with col5:
                fig = plot_school_graduation_share_pie(grad_data, selected_school=selected_school, selected_year=selected_year)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("⚠️ No data available to render graduation share pie chart for the selected school and year.")

            with col6:
                fig = plot_school_graduation_share_pie_by_unitid(grad_data, selected_unitid=selected_unitid_for_pie, selected_year=selected_year)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("⚠️ No valid graduation data found for the selected school and year.")

            fig = plot_graduation_by_race_treemap(grad_data, selected_unitid=selected_unitid, selected_year=selected_years[-1])
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.warning("⚠️ No years found for the selected school.")
    else:
        st.warning("⚠️ No schools available for graduation data.")

# You can uncomment this if needed
# fig = plot_graduation_by_gender_bar(grad_data, selected_unitid=selected_unitid, selected_year=selected_years[-1])
# st.plotly_chart(fig, use_container_width=True)

# 🔸🔸 Financial Aid Page 🔸🔸
elif st.session_state.active_page == "Financial Aid":
    st.markdown("""### :orange[Financial Aid]""")
    sfa_data = load_data(sfa_fpath)
    
    # Get sorted list of all institution names
    all_schools = sorted(sfa_data["university_name"].dropna().unique())
    default_school = "New Jersey Institute of Technology"

    # Create and display the top 20 institutions by total aid chart
    fig = plot_top20_institutions_by_total_aid(sfa_data)
    st.plotly_chart(fig, use_container_width=True)
    st.button("𝒾", help=get_top20_institutions_aid_help())

    # School selection dropdown
    selected_school = st.selectbox(
        "Select an Institution",
        all_schools,
        index=all_schools.index(default_school) if default_school in all_schools else 0
    )

    # Get UNITID for selected school
    selected_unitid = sfa_data[sfa_data["university_name"] == selected_school]["unitid"].iloc[0]

    # Create and display the net price chart
    fig = plot_net_price_by_income(sfa_data, selected_school)
    st.plotly_chart(fig, use_container_width=True)
    st.button("𝒾", help=get_net_price_by_income_help())

    # Create and display the aid type breakdown chart
    fig = plot_aid_type_breakdown_percent(sfa_data, selected_school)
    st.plotly_chart(fig, use_container_width=True)
    st.button("𝒾", help=get_aid_type_breakdown_help())
