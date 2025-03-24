import streamlit as st
import pandas as pd
import plotly.express as px

# 🔹 Load and filter data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# 🔹 Admission Funnel
def plot_admission_funnel(data):
    """Plots the admission funnel with Applicants, Admissions, and Enrollments as a funnel chart"""
    
    # Aggregate university data
    grouped_data = data.groupby("university_name")[["Applicants_total", "Admissions_total", "Enrolled_total"]].mean().reset_index()
    
    # Melt data for Funnel Chart
    melted_data = grouped_data.melt(id_vars="university_name", 
                                    var_name="Stage", 
                                    value_name="Count")

    # Sort to ensure the funnel order is correct
    stage_order = ["Applicants_total", "Admissions_total", "Enrolled_total"]
    melted_data["Stage"] = pd.Categorical(melted_data["Stage"], categories=stage_order, ordered=True)

    # Create a Funnel Chart
    fig = px.funnel(
        melted_data, 
        x="Count", 
        y="Stage", 
        color="Stage", 
        title="Admission Funnel: Applicants to Enrollments",
        labels={"Stage": "Admission Stages", "Count": "Number of Students"},
        category_orders={"Stage": stage_order}
    )

    # Adjust layout
    fig.update_layout(
        width=1000,  # Adjust width
        height=500,  # Adjust height
        margin=dict(l=50, r=50, t=80, b=100)  # Add margin for readability
    )

    return fig

# 🔹 Bar Chart
def create_bar_chart(data, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        st.warning("Please select at least one school and one year.")
        return None

    filtered_data = data[data["university_name"].isin(selected_schools) & data["year"].isin(selected_years)]
    
    if filtered_data.empty:
        st.warning("No data available for the selected schools and years.")
        return None

    pivot_data = filtered_data.pivot_table(index=["year", "university_name"], columns="level_of_study", 
                                           values="headcount", aggfunc="sum").reset_index()

    pivot_data["university_name"] = pivot_data["university_name"].apply(lambda x: x[:15] + "..." if len(x) > 15 else x)
    melted_data = pd.melt(pivot_data, id_vars=["year", "university_name"], var_name="Level of Study", value_name="Headcount")

    fig = px.bar(melted_data, 
                 x="university_name", 
                 y="Headcount", 
                 color="Level of Study", 
                 title=f"Enrollment Comparison for {', '.join(map(str, selected_years))}",
                 labels={"university_name": "Institution", "Headcount": "Headcount"},
                 text_auto=True, barmode='group', facet_col="year")

    
    fig.update_layout(
        width=800 + (len(selected_years) * 250),  # Expand dynamically
        height=600,
        xaxis_title="Institution",
        yaxis_title="Headcount",
        xaxis_tickangle=0,  # Make labels readable
        legend_title="Level of Study",
    )

    return fig

# 🔹 Pie Chart for NJIT vs Other Schools
def create_pie_chart(data, selected_years):
    filtered_data = data[data["year"].isin(selected_years)]
    
    if filtered_data.empty:
        return None

    njit_mask = filtered_data["university_name"] == "New Jersey Institute of Technology"
    njit_headcount = filtered_data.loc[njit_mask, "headcount"].sum()
    other_headcount = filtered_data.loc[~njit_mask, "headcount"].sum()

    pie_data = pd.DataFrame({
        "University": ["New Jersey Institute of Technology", "Other Schools"],
        "Headcount": [njit_headcount, other_headcount]
    })

    fig = px.pie(pie_data, names="University", values="Headcount",
                 title=f"NJIT vs Other Schools Headcount for {', '.join(map(str, selected_years))}",
                 hole=0.3)

    return fig

# 🔹 Pie Chart for Selected Schools
def create_school_pie_chart(data, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        return None

    filtered_data = data[data["university_name"].isin(selected_schools) & data["year"].isin(selected_years)]
    
    if filtered_data.empty:
        return None

    school_totals = filtered_data.groupby("university_name")["headcount"].sum().reset_index()

    fig = px.pie(school_totals, names="university_name", values="headcount",
                 title=f"Enrollment Proportion Among Selected Schools ({', '.join(map(str, selected_years))})",
                 hole=0.3)

    return fig

# 🔹 Streamlit App Layout
st.title("Enrollment Analysis Dashboard")

# Select years
selected_years = st.multiselect("Select Years", [2018, 2019, 2020, 2021, 2022, 2023], default=[2022])
effy_fpath = "effy/NJ_enrollment_data.csv"
adms_fpath = "adm/NJ_admission_data.csv"
effy_data = load_data(effy_fpath)
adms_data = load_data(adms_fpath)

filtered_effy = effy_data[effy_data["year"].isin(selected_years)]

if filtered_effy.empty:
    st.warning(f"No data available for the selected years: {', '.join(map(str, selected_years))}")
if adms_data.empty:
    st.warning("No data found in the admission dataset.")
else:
    # Select schools
    all_schools = sorted(filtered_effy["university_name"].unique()) 
    effyschools = st.multiselect("Select Schools to Compare", all_schools, default=all_schools[:5])

    # 🔹 First Row
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Enrollment Comparison")
        st.plotly_chart(create_bar_chart(filtered_effy, effyschools, selected_years), use_container_width=True)

    with col2:
        st.subheader("New Jersey Institute of Technology (NJIT) Headcounts Portion in New Jersey")
        st.plotly_chart(create_pie_chart(filtered_effy, selected_years), use_container_width=True)
        

    # 🔹 Second Row
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Enrollment Proportion Among Selected Schools")
        st.plotly_chart(create_school_pie_chart(filtered_effy, effyschools, selected_years), use_container_width=True)

    with col4:
        st.subheader("Admission Funnel")
        filtered_adms = adms_data[adms_data["university_name"].isin(effyschools)]
        st.plotly_chart(plot_admission_funnel(filtered_adms), use_container_width=True)


    
