import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
        title=f"{selected_name} Share of Total Graduates in New Jersey ({selected_year})",
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

def plot_graduation_funnel(df, selected_institution_id=None, selected_year=None, selected_grad_type=None):
    """
    Creates a graduation funnel chart using dbt-processed graduation data.
    
    Args:
        df: DataFrame with dbt-processed graduation data
        selected_institution_id: Filter by specific institution ID
        selected_year: Filter by specific survey year
        selected_grad_type: Filter by specific graduation type (e.g., "Bachelor's or equiv subcohort (4-yr institution)")
    
    Returns:
        Plotly funnel chart figure
    """
    
    # Create a copy to avoid modifying original data
    df_filtered = df.copy()
    
    # Apply filters
    if selected_institution_id:
        df_filtered = df_filtered[df_filtered["INSTITUTION_ID"] == selected_institution_id]
    if selected_year:
        df_filtered = df_filtered[df_filtered["SURVEY_YEAR"] == selected_year]
    if selected_grad_type:
        df_filtered = df_filtered[df_filtered["GRAD_TYPE"] == selected_grad_type]
    
    # Define the funnel stages in logical order - using actual GRAD_TYPE values
    funnel_stages = [
        "Bachelor's or equiv subcohort (4-yr institution) noncompleters still enrolled",
        "Bachelor's or equiv subcohort (4-yr institution) Transfer-out students",
        "Bachelor's or equiv subcohort (4-yr institution), No longer enrolled",
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 6 years",
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 5 years", 
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 4 years or less",
        "4-year institutions, Adjusted cohort (revised cohort minus exclusions)",
    ]
    
    # Create shorter display names for the chart labels
    display_names = [
        "Still Enrolled (Noncompleters)",
        "Transfer-out Students",
        "No Longer Enrolled",
        "Graduated in 6 Years",
        "Graduated in 5 Years",
        "Graduated in 4 Years or Less",

        "Adjusted Cohort",
    ]
    
    # First, find the adjusted cohort size (our baseline for percentages) - MUST be same year
    if selected_year:
        # If year is specified, ensure we only look at that year for baseline
        baseline_df = df_filtered[
            (df_filtered["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) adjusted cohort (revised cohort minus exclusions)") &
            (df_filtered["SURVEY_YEAR"] == selected_year)
        ]
        
        if baseline_df.empty:
            # Fallback to revised cohort if adjusted cohort not found for that year
            baseline_df = df_filtered[
                (df_filtered["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution)") &
                (df_filtered["SURVEY_YEAR"] == selected_year)
            ]
    else:
        # If no year specified, use the year from the first available data
        available_years = df_filtered["SURVEY_YEAR"].unique()
        if len(available_years) > 0:
            # Use the first available year as our baseline year
            baseline_year = available_years[0]
            baseline_df = df_filtered[
                (df_filtered["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) adjusted cohort (revised cohort minus exclusions)") &
                (df_filtered["SURVEY_YEAR"] == baseline_year)
            ]
            
            if baseline_df.empty:
                # Fallback to revised cohort
                baseline_df = df_filtered[
                    (df_filtered["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution)") &
                    (df_filtered["SURVEY_YEAR"] == baseline_year)
                ]
        else:
            baseline_df = pd.DataFrame()  # Empty DataFrame
    
    if baseline_df.empty:
        # If still no baseline found, return empty chart
        fig = go.Figure()
        fig.add_annotation(
            text="No cohort baseline data found for the selected filters",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(title="Graduation Outcomes of Bachelor’s Cohort (4-Year Institutions) - No Baseline Data")
        return fig
    
    baseline_cohort_size = baseline_df["GR_TOTAL_ALL"].sum()
    baseline_year = baseline_df["SURVEY_YEAR"].iloc[0]
    
    # Now filter all outcome stages to use ONLY the same year as the baseline
    df_filtered = df_filtered[df_filtered["SURVEY_YEAR"] == baseline_year]
    
    # Initialize data for funnel
    stage_data = []
    
    for i, stage in enumerate(funnel_stages):
        # Filter data for this stage - using GRAD_TYPE since these are the actual type values
        stage_df = df_filtered[df_filtered["GRAD_TYPE"] == stage]
        
        if not stage_df.empty:
            # Sum the total students for this stage
            total_students = stage_df["GR_TOTAL_ALL"].sum()
            
            if total_students > 0:  # Only include stages with students
                # Calculate percentage of baseline cohort
                percentage = (total_students / baseline_cohort_size) * 100
                stage_data.append({
                    "Stage": display_names[i],  # Use shorter display name
                    "Students": total_students,
                    "Percentage": percentage,
                    "Formatted_Count": f"{int(total_students):,} ({percentage:.1f}%)"
                })
    
    if not stage_data:
        # Return empty chart if no data
        fig = go.Figure()
        fig.add_annotation(
            text="No data available for the selected filters",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(title="Graduation Outcomes of Bachelor’s Cohort (4-Year Institutions) - No Data Available")
        return fig
    
    # Create DataFrame for plotting
    funnel_df = pd.DataFrame(stage_data)
    
    # Create a horizontal bar chart that looks like a funnel (decreasing widths)
    fig = go.Figure(go.Bar(
        y=funnel_df["Stage"],
        x=funnel_df["Students"],
        orientation='h',
        text=funnel_df["Formatted_Count"],
        textposition='inside',
        marker=dict(
            color=px.colors.sequential.Blues,
            line=dict(width=1, color="white")
        )
    ))
    
    # Update layout
    fig.update_layout(
        title={
            "text": f"Graduation Outcomes of Bachelor’s Cohort (4-Year Institutions)",
            "x": 0.5,
            "xanchor": "center"
        },
        height=600,
        showlegend=False,
        margin=dict(t=80, l=20, r=20, b=20),
        font=dict(size=12)
    )
    
    # Update axes
    fig.update_xaxes(title_text="Number of Students")
    fig.update_yaxes(title_text="Graduation Status", categoryorder='array', categoryarray=display_names)
    
    return fig

def plot_university_wide_graduation_rate(data, selected_unitid=None):
    df = data.copy()
    
    # Convert to numeric and handle missing values
    df["GR_TOTAL_ALL"] = pd.to_numeric(df["GR_TOTAL_ALL"], errors="coerce").fillna(0)
    
    # Filter for specific institution if provided
    if selected_unitid:
        df = df[df["INSTITUTION_ID"] == selected_unitid]
    
    # Keep only the specific rows we need for numerator and denominator
    df = df[
        (df["GRAD_TYPE"].str.contains("Bachelor's or equiv subcohort", na=False)) |
        (df["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) adjusted cohort (revised cohort minus exclusions)")
    ]
    
    # NUMERATOR: Get graduates (completers within 4 years or less)
    graduates_4yr_df = df[df["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 4 years or less"].copy()
    # NUMERATOR: Get graduates (completers within 5 years)
    graduates_5yr_df = df[df["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 5 years"].copy()
    # NUMERATOR: Get graduates (completers within 6 years)
    graduates_6yr_df = df[df["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 6 years"].copy()
    
    # DENOMINATOR: Get total cohort (adjusted cohort minus exclusions)
    cohort_df = df[df["GRAD_TYPE"] == "Bachelor's or equiv subcohort (4-yr institution) adjusted cohort (revised cohort minus exclusions)"].copy()
    
    # Group by year and sum the totals
    graduates_4yr_by_year = graduates_4yr_df.groupby("SURVEY_YEAR")["GR_TOTAL_ALL"].sum().reset_index()
    graduates_5yr_by_year = graduates_5yr_df.groupby("SURVEY_YEAR")["GR_TOTAL_ALL"].sum().reset_index()
    graduates_6yr_by_year = graduates_6yr_df.groupby("SURVEY_YEAR")["GR_TOTAL_ALL"].sum().reset_index()
    cohort_by_year = cohort_df.groupby("SURVEY_YEAR")["GR_TOTAL_ALL"].sum().reset_index()
    
    # Merge the dataframes for 4-year rate
    merged_4yr_df = pd.merge(graduates_4yr_by_year, cohort_by_year, 
                            on="SURVEY_YEAR", 
                            suffixes=("_graduates", "_cohort"))
    
    # Merge the dataframes for 5-year rate
    merged_5yr_df = pd.merge(graduates_5yr_by_year, cohort_by_year, 
                            on="SURVEY_YEAR", 
                            suffixes=("_graduates", "_cohort"))
    
    # Merge the dataframes for 6-year rate
    merged_6yr_df = pd.merge(graduates_6yr_by_year, cohort_by_year, 
                            on="SURVEY_YEAR", 
                            suffixes=("_graduates", "_cohort"))
    
    # Calculate graduation rates
    merged_4yr_df["graduation_rate"] = (merged_4yr_df["GR_TOTAL_ALL_graduates"] / 
                                       merged_4yr_df["GR_TOTAL_ALL_cohort"] * 100).round(2)
    merged_5yr_df["graduation_rate"] = (merged_5yr_df["GR_TOTAL_ALL_graduates"] / 
                                       merged_5yr_df["GR_TOTAL_ALL_cohort"] * 100).round(2)
    merged_6yr_df["graduation_rate"] = (merged_6yr_df["GR_TOTAL_ALL_graduates"] / 
                                       merged_6yr_df["GR_TOTAL_ALL_cohort"] * 100).round(2)
    
    # Add graduation type labels
    merged_4yr_df["graduation_type"] = "4-Year"
    merged_5yr_df["graduation_type"] = "5-Year"
    merged_6yr_df["graduation_type"] = "6-Year"
    
    # Display cohort year as survey year minus 6
    merged_4yr_df["COHORT_YEAR"] = pd.to_numeric(merged_4yr_df["SURVEY_YEAR"], errors="coerce").astype("Int64") - 6
    merged_5yr_df["COHORT_YEAR"] = pd.to_numeric(merged_5yr_df["SURVEY_YEAR"], errors="coerce").astype("Int64") - 6
    merged_6yr_df["COHORT_YEAR"] = pd.to_numeric(merged_6yr_df["SURVEY_YEAR"], errors="coerce").astype("Int64") - 6
    
    # Combine both dataframes
    combined_df = pd.concat([merged_4yr_df, merged_5yr_df, merged_6yr_df], ignore_index=True)
    
    # Sort by cohort year
    combined_df = combined_df.sort_values("COHORT_YEAR")
    
    # Create the line chart
    fig = px.line(
        combined_df,
        x="COHORT_YEAR",
        y="graduation_rate",
        color="graduation_type",
        markers=True,
        title="University Wide Graduation Rate",
        labels={
            "COHORT_YEAR": "Cohort Year",
            "graduation_rate": "Graduation Rate (%)",
            "graduation_type": "Graduation Type"
        },
        color_discrete_sequence=["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blue, orange, and green colors
    )
    
    # Update layout
    fig.update_layout(
        yaxis=dict(
            ticksuffix="%",
            range=[0, 100],
            gridcolor="lightgray",
            zerolinecolor="lightgray"
        ),
        xaxis=dict(
            dtick=1,
            gridcolor="lightgray",
            zerolinecolor="lightgray"
        ),
        height=500,
        plot_bgcolor="white",
        # title_x=0.5
    )
    
    # Update traces
    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8)
    )
    
    return fig
