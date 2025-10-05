import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 🔹 Load data with caching
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# 🔹 Total Enrollment Bar Chart
def create_total_enrollment_bar_chart(adms_data, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        st.warning("Please select at least one school and one year.")
        return None

    filtered_data = adms_data[
        adms_data["university_name"].isin(selected_schools) &
        adms_data["year"].isin(selected_years)
    ]

    if filtered_data.empty:
        st.warning("No data available for the selected schools and years.")
        return None

    chart_data = filtered_data[[
        "university_name", "year", "Enrolled_total"]].copy()
    chart_data["Enrolled_total"] = pd.to_numeric(
        chart_data["Enrolled_total"], errors='coerce').fillna(0)
    chart_data["year"] = chart_data["year"].astype(
        str)  # Make year categorical

    fig = px.bar(
        chart_data,
        x="university_name",
        y="Enrolled_total",
        color="university_name",  # Now treated as discrete
        title=f"Total Fall Undergraduate Enrollment (Stacked by Year) ({', '.join(chart_data['year'].unique())})",
        labels={"university_name": "Institution",
                "Enrolled_total": "Total Enrollment"},
        barmode='group',
        text="Enrolled_total",
        color_discrete_sequence=px.colors.qualitative.G10,
    )

    fig.update_layout(
        width=800 + (len(selected_years) * 250),
        height=600,
        xaxis_tickangle=0,
        showlegend=False,
        coloraxis_showscale=False  # Not needed anymore, but just in case
    )

    return fig

# 🔹 Gender Enrollment Bar Chart
def create_gender_enrollment_bar_chart(adms_data, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        st.warning("Please select at least one school and one year.")
        return None

    filtered_data = adms_data[
        adms_data["university_name"].isin(selected_schools) &
        adms_data["year"].isin(selected_years)
    ]

    if filtered_data.empty:
        st.warning("No data available for the selected schools and years.")
        return None

    rows = []
    for _, row in filtered_data.iterrows():
        try:
            men = float(row["Enrolled__men"])
        except:
            men = 0
        try:
            women = float(row["Enrolled__women"])
        except:
            women = 0

        rows.append({"university_name": row["university_name"],
                    "year": row["year"], "Gender": "Men", "Headcount": men})
        rows.append({"university_name": row["university_name"],
                    "year": row["year"], "Gender": "Women", "Headcount": women})

    chart_data = pd.DataFrame(rows)

    fig = px.bar(
        chart_data,
        x="university_name",
        y="Headcount",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Dark24,
        facet_col="year",
        title=f"Enrollment by Gender ({', '.join(map(str, selected_years))})",
        labels={"university_name": "Institution", "Headcount": "Headcount"},
        barmode='group',
        text_auto=True
    )

    fig.update_layout(
        width=800 + (len(selected_years) * 250),
        height=600,
        xaxis_tickangle=0
    )

    return fig

# 🔹 Full-Time vs Part-Time Enrollment Trend Over Time
def create_full_vs_part_time_trend(adms_data, selected_school):
    if not selected_school:
        st.warning("Please select a school.")
        return None

    data = adms_data[adms_data["university_name"] == selected_school][
        ["year", "Enrolled_full_time_total", "Enrolled_part_time_total"]
    ].copy()

    if data.empty:
        st.warning(f"No enrollment data available for {selected_school}.")
        return None

    data["Enrolled_full_time_total"] = pd.to_numeric(
        data["Enrolled_full_time_total"], errors="coerce").fillna(0)
    data["Enrolled_part_time_total"] = pd.to_numeric(
        data["Enrolled_part_time_total"], errors="coerce").fillna(0)

    grouped = data.groupby("year")[
        ["Enrolled_full_time_total", "Enrolled_part_time_total"]].sum().reset_index()

    melted = grouped.melt(
        id_vars="year", var_name="Enrollment Type", value_name="Headcount")

    fig = px.line(
        melted,
        x="year",
        y="Headcount",
        color="Enrollment Type",
        markers=True,  # ✅ Optional: add dots at each point
        color_discrete_sequence=["#2A2C78", "#97BAEC"],
        title=f"Full-Time vs Part-Time Enrollment Trend Over Time",
        labels={"year": "Year", "Headcount": "Student Count"},
    )

    fig.update_layout(
        height=500,
        xaxis=dict(dtick=1),
        yaxis_title="Students Enrolled",
        xaxis_title="Year",
        showlegend=False,
    )

    fig.update_traces(line=dict(width=2), marker=dict(size=10))

    return fig

def create_full_vs_part_time_trend_multiple(adms_data, selected_schools):
    if not selected_schools:
        st.warning("Please select at least one school.")
        return None

    data = adms_data[adms_data["university_name"].isin(selected_schools)][
        ["year", "university_name", "Enrolled_full_time_total", "Enrolled_part_time_total"]
    ].copy()

    if data.empty:
        st.warning(f"No enrollment data available for the selected schools.")
        return None

    data["Enrolled_full_time_total"] = pd.to_numeric(
        data["Enrolled_full_time_total"], errors="coerce").fillna(0)
    data["Enrolled_part_time_total"] = pd.to_numeric(
        data["Enrolled_part_time_total"], errors="coerce").fillna(0)

    # Melt for better plotting
    melted = data.melt(
        id_vars=["year", "university_name"],
        value_vars=["Enrolled_full_time_total", "Enrolled_part_time_total"],
        var_name="Enrollment Type",
        value_name="Headcount"
    )

    # Make Enrollment Type cleaner
    melted["Enrollment Type"] = melted["Enrollment Type"].replace({
        "Enrolled_full_time_total": "Full-Time",
        "Enrolled_part_time_total": "Part-Time"
    })

    fig = px.line(
        melted,
        x="year",
        y="Headcount",
        color="university_name",         
        line_dash="Enrollment Type",
        markers=True,
        title=f"Full-Time vs Part-Time Enrollment Trends Across Selected Institutions",
        labels={"year": "Year", "Headcount": "Student Count"},
        color_discrete_sequence=px.colors.qualitative.G10
    )

    fig.update_layout(
        height=600,
        xaxis=dict(dtick=1),
        yaxis_title="Students Enrolled",
        xaxis_title="Year",
    )

    return fig


# 🔹 Admission/Enrollment Rate by School
def create_admission_yield_rate_chart(adms_data, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        st.warning("Please select at least one school and year.")
        return None

    df = adms_data.copy()
    df["Applicants_total"] = pd.to_numeric(
        df["Applicants_total"], errors="coerce").fillna(0)
    df["Admissions_total"] = pd.to_numeric(
        df["Admissions_total"], errors="coerce").fillna(0)
    df["Enrolled_total"] = pd.to_numeric(
        df["Enrolled_total"], errors="coerce").fillna(0)

    df = df[df["university_name"].isin(
        selected_schools) & df["year"].isin(selected_years)]

    if df.empty:
        st.warning("No data available for the selected schools and years.")
        return None

    # Compute rates per school per year
    df["Admission Rate"] = df["Admissions_total"] / df["Applicants_total"]
    df["Yield Rate"] = df["Enrolled_total"] / df["Admissions_total"]

    # Clean up invalid values
    df = df.replace([float("inf"), float("nan")], 0)

    # Melt for bar chart
    melted = df.melt(
        id_vars=["university_name", "year"],
        value_vars=["Admission Rate", "Yield Rate"],
        var_name="Rate Type",
        value_name="Rate"
    )
    melted["Rate (%)"] = (melted["Rate"] * 100).round(2)
    melted["year"] = melted["year"].astype(str)
    fig = px.bar(
        melted,
        x="university_name",
        y="Rate (%)",
        color="university_name",
        color_discrete_sequence=px.colors.qualitative.G10,
        facet_col="Rate Type",
        barmode="group",
        text="Rate (%)",
        labels={"university_name": "Institution", "year": "Year"},
        title="Admission & Yield Rates by School and Year"
    )

    fig.update_layout(
        height=600,
        xaxis_tickangle=45,
        width=1000 + len(selected_schools) * 50,
    )

    return fig

# 🔹 Admission Funnel
def plot_admission_funnel(data, school_name, selected_year):
    """Plots the admission funnel for a specific school and year."""

    # Filter by school and year
    school_data = data[
        (data["university_name"] == school_name) & 
        (data["year"] == selected_year)
    ]

    if school_data.empty:
        st.warning(f"No admission data available for {school_name} in {selected_year}.")
        return None

    # Extract the row directly (no groupby)
    counts = school_data[["Applicants_total", "Admissions_total", "Enrolled_total"]].iloc[0]

    # Prepare data for funnel
    melted_data = pd.DataFrame({
        "Stage": ["Applicants_total", "Admissions_total", "Enrolled_total"],
        "Count": [counts["Applicants_total"], counts["Admissions_total"], counts["Enrolled_total"]],
    })

    stage_order = ["Applicants_total", "Admissions_total", "Enrolled_total"]
    melted_data["Stage"] = pd.Categorical(melted_data["Stage"], categories=stage_order, ordered=True)

    fig = px.funnel(
        melted_data,
        x="Count",
        y="Stage",
        color="Stage",
        title=f"Admission Funnel: {school_name} ({selected_year})",
        labels={"Stage": "Admission Stages", "Count": "Number of Students"},
        category_orders={"Stage": stage_order},
        color_discrete_sequence=["#2C43B8", "#6987D5", "#BBDFFA"]
    )

    fig.update_layout(
        xaxis=dict(
            tickformat=".0f",           # Whole numbers
            separatethousands=True,     # Show commas (e.g. 13,933)
            exponentformat="none",      # Disable scientific or suffixes like "k"
            tickprefix="",              # No prefix
            ticksuffix="",              # No suffix
        )
    )
    fig.update_traces(texttemplate="%{x:,}", textposition="inside")

    return fig

# 🔹 Pie Chart
def create_njit_vs_others_pie(adms_data, selected_years):
    df = adms_data.copy()

    # Clean + filter
    df["Enrolled_total"] = pd.to_numeric(
        df["Enrolled_total"], errors="coerce").fillna(0)
    df = df[df["year"].isin(selected_years)]

    if df.empty:
        st.warning("No enrollment data available for the selected years.")
        return None

    # Aggregate total enrollment
    njit_name = "New Jersey Institute of Technology"
    njit_total = df[df["university_name"] == njit_name]["Enrolled_total"].sum()
    others_total = df[df["university_name"]
                      != njit_name]["Enrolled_total"].sum()

    pie_data = pd.DataFrame({
        "School": ["NJIT", "All Other NJ Schools"],
        "Enrolled": [njit_total, others_total]
    })

    fig = px.pie(
        pie_data,
        names="School",
        values="Enrolled",
        title=f"NJIT vs Other NJ Schools Undergraduate Enrollment ({', '.join(map(str, selected_years))})",
        hole=0.3,
        color_discrete_sequence=["#292361", "#bfb8fc"]
    )

    return fig

# 🔹 Stacked Bar Chart
def plot_njit_share_change(df, njit_name="New Jersey Institute of Technology"):
    df["Enrolled_total"] = pd.to_numeric(df["Enrolled_total"], errors="coerce").fillna(0)

    # Aggregate total enrollment by year and university
    grouped = df.groupby(["year", "university_name"])["Enrolled_total"].sum().reset_index()

    # Compute NJIT vs Others
    grouped["School Group"] = grouped["university_name"].apply(
        lambda name: njit_name if name == njit_name else "All Other NJ Schools"
    )
    totals = grouped.groupby(["year", "School Group"])["Enrolled_total"].sum().reset_index()

    # Pivot to calculate NJIT share
    pivot = totals.pivot(index="year", columns="School Group", values="Enrolled_total").fillna(0)
    pivot["Total"] = pivot.sum(axis=1)
    pivot["NJIT Share (%)"] = (pivot[njit_name] / pivot["Total"]) * 100
    pivot["Share Change (%)"] = pivot["NJIT Share (%)"].diff()

    # Format label for annotation
    def format_label(change):
        if pd.isna(change):
                return ""
        elif change >= 0:
            return f"<span style='color:#00c853'>▲ {change:.1f}%</span>"  # Green
        else:
            return f"<span style='color:#d32f2f'>▼ {abs(change):.1f}%</span>"  # Red

    pivot["Annotation"] = pivot["Share Change (%)"].apply(format_label)
    pivot = pivot.reset_index()

    # Melt for stacked bar chart
    melt = pivot.melt(id_vars=["year", "Annotation"], value_vars=[njit_name, "All Other NJ Schools"],
                      var_name="School Group", value_name="Enrolled_total")

    # Set color theme
    color_map = {
        njit_name: "#bfb8fc",
        "All Other NJ Schools": "#292361"
    }

    fig = px.bar(
        melt,
        x="year",
        y="Enrolled_total",
        color="School Group",
        barmode="stack",
        color_discrete_map=color_map,
        title="Yearly Enrollment and Change in NJIT’s Share of Total Enrollment",
        labels={"Enrolled_total": "Enrollment", "year": "Year"}
    )

    # Add annotation: only once per year above NJIT bar
    for year in pivot["year"]:
        njit_enrollment = melt[(melt["year"] == year) & (melt["School Group"] == njit_name)]["Enrolled_total"].values[0]
        annotation_text = pivot[pivot["year"] == year]["Annotation"].values[0]

        if annotation_text:
            fig.add_annotation(
                x=year,
                y=njit_enrollment,
                text=annotation_text,
                showarrow=False,
                yshift=10,
                font=dict(size=12),
                align="center"
            )

    fig.update_layout(
        height=600,
        yaxis_title="Enrollment",
        xaxis_title="Year",
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        legend=dict(
            orientation="h",  # horizontal layout
            yanchor="bottom",
            y=-0.3,           # move legend below chart
            xanchor="center",
            x=0.5
    ))

    return fig

# 🔹 Total Enrollment Bar Chart using DBT-processed data
def plot_total_enrollment_bar_chart(enrollment_data, institution_mapping, selected_schools, selected_years):
    if not selected_schools or not selected_years:
        st.warning("Please select at least one school and one year.")
        return None

    # Filter for total enrollment data (All students total)
    total_data = enrollment_data[
        enrollment_data["STUDENT_LEVEL_AND_DEGREE_STATUS"] == "All students total"
    ].copy()
    
    if total_data.empty:
        st.warning("No total enrollment data found in the dataset.")
        return None

    # Convert year to integer for filtering
    total_data["SURVEY_YEAR"] = pd.to_numeric(total_data["SURVEY_YEAR"], errors='coerce')
    
    # Filter by selected years
    total_data = total_data[total_data["SURVEY_YEAR"].isin(selected_years)]
    
    if total_data.empty:
        st.warning("No data available for the selected years.")
        return None

    # Merge with institution mapping to get institution names
    merged_data = total_data.merge(
        institution_mapping, 
        left_on="INSTITUTION_ID", 
        right_on="unitid", 
        how="left"
    )
    
    # Filter by selected schools
    merged_data = merged_data[merged_data["inst_name"].isin(selected_schools)]
    
    if merged_data.empty:
        st.warning("No data available for the selected schools and years.")
        return None

    # Prepare chart data
    chart_data = merged_data[[
        "inst_name", "SURVEY_YEAR", "GRAND_TOTAL"
    ]].copy()
    
    # Rename columns for consistency with original function
    chart_data = chart_data.rename(columns={
        "inst_name": "university_name",
        "SURVEY_YEAR": "year",
        "GRAND_TOTAL": "Enrolled_total"
    })
    
    # Convert enrollment to numeric
    chart_data["Enrolled_total"] = pd.to_numeric(
        chart_data["Enrolled_total"], errors='coerce').fillna(0)
    chart_data["year"] = chart_data["year"].astype(str)  # Make year categorical

    fig = px.bar(
        chart_data,
        x="university_name",
        y="Enrolled_total",
        color="university_name",
        title=f"Total Fall Enrollment (DBT-processed) ({', '.join(chart_data['year'].unique())})",
        labels={"university_name": "Institution",
                "Enrolled_total": "Total Enrollment"},
        barmode='group',
        text="Enrolled_total",
        color_discrete_sequence=px.colors.qualitative.G10,
    )

    fig.update_layout(
        width=800 + (len(selected_years) * 250),
        height=600,
        xaxis_tickangle=0,
        showlegend=False,
        coloraxis_showscale=False
    )

    return fig

# 🔹 Enrollment Over Years for Selected School
def plot_enrollment_over_years(enrollment_data, institution_id=185828):
    
    if not institution_id:
        st.warning("Please provide an institution ID.")
        return None
    
    for level in enrollment_data['STUDENT_LEVEL_AND_DEGREE_STATUS'].unique():
        print(f"  - '{level}'")
    
    # Filter data for the selected institution and specific student level
    school_data = enrollment_data[
        (enrollment_data['INSTITUTION_ID'] == institution_id) &
        (enrollment_data['STUDENT_LEVEL_AND_DEGREE_STATUS'] == 'All students, Undergraduate total')
    ].copy()
    
    if school_data.empty:
        st.error(f"No enrollment data found for institution ID: {institution_id}")
        return None
    
    # Convert survey_year to numeric and sort
    school_data['SURVEY_YEAR'] = pd.to_numeric(school_data['SURVEY_YEAR'])
    school_data = school_data.sort_values('SURVEY_YEAR')
    
    # Use the data directly (no aggregation needed since we're filtering to specific level)
    yearly_totals = school_data[['SURVEY_YEAR', 'GRAND_TOTAL']].copy()
    
    if yearly_totals.empty:
        st.error(f"No undergraduate enrollment data available for institution ID: {institution_id}")
        return None
    
    # Create the line plot
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x=yearly_totals['SURVEY_YEAR'],
            y=yearly_totals['GRAND_TOTAL'],
            mode='lines+markers',
            name='Total Enrollment',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8),
            hovertemplate='<b>Total Enrollment</b><br>' +
                        'Year: %{x}<br>' +
                        'Enrollment: %{y:,.0f}<br>' +
                        '<extra></extra>'
        )
    )
    
    fig.update_layout(
        height=600,
        showlegend=False
    )
    
    # Update layout
    fig.update_layout(
        title=dict(
            text=f'Undergraduate Enrollment by Year',
            font=dict(size=16)
        ),
        xaxis_title="Year",
        yaxis_title="Enrollment Count",
        hovermode='x unified',
        template='plotly_white',
        margin=dict(l=50, r=50, t=80, b=50)
    )
    
    # Update x-axis
    fig.update_xaxes(
        tickmode='linear',
        tick0=yearly_totals['SURVEY_YEAR'].min(),
        dtick=1,
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray'
    )
    
    # Update y-axis
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        tickformat=','
    )
    
    return fig
