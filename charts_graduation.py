import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def graduation_funnel_chart(df, selected_unitid=None, selected_year=None):
    """
    Creates and returns a Plotly funnel chart showing:
    Adjusted Cohort -> Graduated in 100% -> Graduated in 150% -> Transferred Out
    """

    if selected_unitid:
        df = df[df["unitid"] == selected_unitid]
    if selected_year:
        df = df[df["year"] == selected_year]

    funnel_stages = {
        12: "Initial Bachelor’s Cohort",
        13: "Graduated in 4 Years or Less",
        14: "Graduated in 5 Years",
        15: "Graduated in 6 Years",
        16: "Transferred Out",
    }

    stage_names = []
    student_counts = []

    for code, label in funnel_stages.items():
        count = df[df["Graduation_rate_status_in_cohort"] == code]["Total"].sum()
        stage_names.append(label)
        student_counts.append(count)

    funnel_df = pd.DataFrame({
        "Stage": stage_names,
        "Students": student_counts,
        "Text": [f"{int(v):,}" for v in student_counts]  # format like 13,933
    })

    fig = px.bar(
        funnel_df,
        x="Students",
        y="Stage",
        orientation="h",
        text="Text",  # 👈 use manually formatted text
        title="Graduation Funnel",
        labels={"Stage": "Cohort Status", "Students": "Number of Students"},
        color_discrete_sequence=["#7ddaff"]
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        height=400,
        uniformtext_minsize=8,
        uniformtext_mode='show',
    )

    fig.update_traces(textposition="inside")

    return fig

def plot_graduation_rate_trend(data, selected_unitid=None):
    """
    Plots a line chart showing graduation rates (4, 5, 6 years) over time
    for a specific institution or across all if selected_unitid is None.
    """
    df = data.copy()
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

    # Filter to relevant CHRTSTAT codes
    relevant_codes = {
        12: "Adjusted Cohort",
        13: "Grad ≤ 4 Years",
        14: "Grad in 5 Years",
        15: "Grad in 6 Years"
    }
    df = df[df["Graduation_rate_status_in_cohort"].isin(relevant_codes.keys())]

    if selected_unitid:
        df = df[df["unitid"] == selected_unitid]

    # Pivot data: year x outcome
    pivot = df.pivot_table(
        index=["year"],
        columns="Graduation_rate_status_in_cohort",
        values="Total",
        aggfunc="sum"
    ).reset_index()
    pivot.rename(columns=relevant_codes, inplace=True)

    # Skip if Adjusted Cohort is missing
    if "Adjusted Cohort" not in pivot.columns:
        return None

    # Calculate graduation rates only for available columns
    for label in ["Grad ≤ 4 Years", "Grad in 5 Years", "Grad in 6 Years"]:
        if label in pivot.columns:
            pivot[label] = (pivot[label] / pivot["Adjusted Cohort"] * 100).round(2)

    # Melt for plotting
    available_labels = [col for col in ["Grad ≤ 4 Years", "Grad in 5 Years", "Grad in 6 Years"] if col in pivot.columns]

    melted = pivot.melt(
        id_vars="year",
        value_vars=available_labels,
        var_name="Completion Time",
        value_name="Graduation Rate (%)"
    )

    fig = px.line(
        melted,
        x="year",
        y="Graduation Rate (%)",
        color="Completion Time",
        markers=True,
        title="Graduation Rate Trend Over Time",
        labels={"year": "Year", "Graduation Rate (%)": "Graduation Rate (%)"},
        color_discrete_sequence=px.colors.qualitative.Set1
    )

    fig.update_layout(
        yaxis=dict(ticksuffix="%"),
        xaxis=dict(dtick=1),
        height=500
    )

    return fig

def plot_graduation_by_race_treemap(data, selected_unitid=None, selected_year=None):
    df = data.copy()
    df["Total"] = pd.to_numeric(df["Total"], errors="coerce").fillna(0)

    if selected_unitid:
        df = df[df["unitid"] == selected_unitid]
    if selected_year:
        df = df[df["year"] == selected_year]

    # Only CHRTSTAT 13 = completed within 4 years of less
    df = df[df["Graduation_rate_status_in_cohort"] == 13]

    race_cols = {
        "American_Indian_or_Alaska_Native_total": "American Indian or Alaska Native",
        "Asian_total": "Asian",
        "Black_or_African_American_total": "Black or African American",
        "Hispanic_total": "Hispanic",
        "Native_Hawaiian_or_Other_Pacific_Islander_total": "Native Hawaiian or Pacific Islander",
        "White_total": "White",
        "Two_or_more_races_total": "Two or More Races",
        "Race_ethnicity_unknown_total": "Unknown",
        "U_S__Nonresident_total": "Nonresident Alien"
    }

    available_cols = [col for col in race_cols if col in df.columns]
    if not available_cols:
        return None

    totals = df[available_cols].sum().dropna().astype(int).to_dict()

    labels = [race_cols[k] for k in totals.keys()]
    values = list(totals.values())

    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=[""] * len(labels),
        values=values,
        marker=dict(colors=values, colorscale="Blues",line=dict(width=0) ),
        textinfo="label+value+percent root"
    ))

    fig.update_layout(
        title="Graduation by Race/Ethnicity (Completed within ≤ 4 Years)",
        margin=dict(t=50, l=25, r=25, b=25)
    )

    return fig

def plot_graduation_by_gender_bar(data, selected_unitid=None, selected_year=None):
    """
    Plots a grouped bar chart showing graduation outcomes by gender
    for a selected school and year.
    """

    df = data.copy()
    df["Total_men"] = pd.to_numeric(df["Total_men"], errors="coerce").fillna(0)
    df["Total_women"] = pd.to_numeric(df["Total_women"], errors="coerce").fillna(0)

    if selected_unitid:
        df = df[df["unitid"] == selected_unitid]
    if selected_year:
        df = df[df["year"] == selected_year]

    # Select relevant GRTYPE codes (based on Bachelor’s cohort: GRTYPE 8)
    df = df[df["Cohort_type"] == '8']  # Replace with your actual GRTYPE column name


    # Graduation outcome codes and labels from CHRTSTAT
    outcome_codes = {
        13: "Completed in 150%",
        14: "Completed in 5 Years",
        15: "Completed in 6 Years",
        16: "Transferred Out",
        31: "Still Enrolled",
        32: "No Longer Enrolled"
    }

    gender_data = []
    for chrtstat_code, label in outcome_codes.items():
        subset = df[df["Graduation_rate_status_in_cohort"] == chrtstat_code]
        men = subset["Total_men"].sum()

        print(men)
        women = subset["Total_women"].sum()
        gender_data.extend([
            {"Outcome": label, "Gender": "Men", "Count": men},
            {"Outcome": label, "Gender": "Women", "Count": women},
        ])

    gender_df = pd.DataFrame(gender_data)

    fig = px.bar(
        gender_df,
        x="Outcome",
        y="Count",
        color="Gender",
        barmode="group",
        title="Graduation Outcomes by Gender",
        labels={"Outcome": "Graduation Outcome", "Count": "Number of Students"},
        color_discrete_map={"Men": "#4ba3c7", "Women": "#f285b3"}
    )

    fig.update_layout(
        xaxis_tickangle=-15,
        height=500
    )

    return fig

def plot_school_graduation_share_pie_by_unitid(df, selected_unitid, selected_year):
    # Filter for the selected year and graduation cohort (graduated = 10)
    df_year = df[(df['year'] == selected_year) & (df['Graduation_rate_status_in_cohort'] == 10)]

    # Total graduates in that year
    total_grads_all = df_year['Total'].sum()

    # Get the selected school's row by unitid
    selected_row = df_year[df_year['unitid'] == selected_unitid]
    if selected_row.empty:
        print(f"No graduation data found for unitid '{selected_unitid}' in {selected_year}.")
        return None

    selected_grads = selected_row['Total'].values[0]
    selected_name = selected_row['university_name'].values[0]
    other_grads = total_grads_all - selected_grads

    pie_data = pd.DataFrame({
        'School': [selected_name, 'All Other NJ Schools'],
        'Graduates': [selected_grads, other_grads]
    })

    fig = px.pie(
        pie_data,
        names='School',
        values='Graduates',
        title=f"Selected School Share of Total Graduates in New Jersey ({selected_year})",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.G10,
    )
    fig.update_traces(textinfo='percent+label',
                      insidetextorientation='horizontal')

    return fig

def plot_school_graduation_share_pie(df, selected_school="New Jersey Institute of Technology", selected_year=None):
    # Filter for the selected year and graduation cohort
    df_year = df[(df['year'] == selected_year) & (df['Graduation_rate_status_in_cohort'] == 10)]

    # Group data
    total_grads_all = df_year['Total'].sum()
    
    # Graduation count for selected school
    selected_row = df_year[df_year['university_name'] == selected_school]
    if selected_row.empty:
        print(f"No graduation data found for '{selected_school}' in {selected_year}.")
        return None

    selected_grads = selected_row['Total'].values[0]
    other_grads = total_grads_all - selected_grads

    pie_data = pd.DataFrame({
        'School': ['NJIT', 'All Other NJ Schools'],
        'Graduates': [selected_grads, other_grads]
    })

    fig = px.pie(
        pie_data,
        names='School',
        values='Graduates',
        title=f"NJIT Share of Total Graduates in New Jersey ({selected_year})",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.G10,
    )
    fig.update_traces(textinfo='percent+label',
                      insidetextorientation='horizontal')

    return fig
