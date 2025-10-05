import plotly.express as px
import pandas as pd

def plot_cohort_graduation_line(df, selected_institution=None):
    """
    Plot graduation rates over time for a selected institution.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Default to NJIT if no institution is selected
    if selected_institution is None:
        selected_institution = 'New Jersey Institute of Technology'
    
    # Filter data for the selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()

    if inst_df.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Compute cohort year (subtract 6)
    inst_df['Cohort Year'] = inst_df['year'] - 6

    # Melt the data for easier plotting
    plot_df = inst_df.melt(
        id_vars=['Cohort Year', 'institution name'],
        value_vars=[
            # 'Graduation rate, total cohort',
            'Graduation rate - Bachelor degree within 4 years, total',
            'Graduation rate - Bachelor degree within 5 years, total',
            'Graduation rate - Bachelor degree within 6 years, total'
        ],
        var_name='Metric',
        value_name='Graduation Rate (%)'
    )

    # Simplify the metric labels for cleaner legend
    label_map = {
        # 'Graduation rate, total cohort': 'Total Cohort',
        'Graduation rate - Bachelor degree within 4 years, total': '4-Year',
        'Graduation rate - Bachelor degree within 5 years, total': '5-Year',
        'Graduation rate - Bachelor degree within 6 years, total': '6-Year'
    }
    plot_df['Metric'] = plot_df['Metric'].map(label_map)

    # Plot with Plotly Express
    fig = px.line(
        plot_df,
        x='Cohort Year',
        y='Graduation Rate (%)',
        color='Metric',
        markers=True,
        title=f"{selected_institution} Graduation Rates by Cohort Year",
        hover_data={'Graduation Rate (%)': ':.1f'}
    )

    fig.update_traces(text=plot_df['Graduation Rate (%)'].round(1), textposition="top center")
    fig.update_layout(
        xaxis=dict(title='Cohort Year', tickmode='linear'),
        yaxis_title='Graduation Rate (%)',
        legend_title='Rate Type',
        template='plotly_white',
    )

    return fig


def plot_cohort_graduation_funnel(df, selected_institution=None, selected_year=None, selected_grad_type=None):
    """
    Creates a graduation funnel chart using dbt-processed graduation data.
    
    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_GRADUATION`
    """
    # Filter data
    df_filtered = df.copy()
    if selected_institution:
        df_filtered = df_filtered[df_filtered["INSTITUTION_NAME"] == selected_institution]
    if selected_year:
        df_filtered = df_filtered[df_filtered["SURVEY_YEAR"] == selected_year]

    # Define stages and display names
    stages = {
        "4-year institutions, Adjusted cohort (revised cohort minus exclusions)": "Total Cohort",
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 4 years or less": "Graduated in 4 Years",
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 5 years": "Graduated in 5 Years",
        "Bachelor's or equiv subcohort (4-yr institution) Completers of bachelor's or equiv degrees in 6 years": "Graduated in 6 Years",
        "Bachelor's or equiv subcohort (4-yr institution), No longer enrolled": "No Longer Enrolled",
        "Bachelor's or equiv subcohort (4-yr institution) Transfer-out students": "Transfer-out",
        "Bachelor's or equiv subcohort (4-yr institution) noncompleters still enrolled": "Still Enrolled"
    }

    # Get baseline cohort size from first available year
    baseline_year = df_filtered["SURVEY_YEAR"].iloc[0] if not selected_year else selected_year
    baseline = df_filtered[
        (df_filtered["GRAD_TYPE"].isin(["Bachelor's or equiv subcohort (4-yr institution) adjusted cohort (revised cohort minus exclusions)", 
                                      "Bachelor's or equiv subcohort (4-yr institution)"]))
        & (df_filtered["SURVEY_YEAR"] == baseline_year)
    ]["GR_TOTAL_ALL"].sum()

    if baseline == 0:
        return px.bar(title="No data available")

    # Create funnel data
    funnel_data = []
    for grad_type, display_name in stages.items():
        count = df_filtered[
            (df_filtered["GRAD_TYPE"] == grad_type) & 
            (df_filtered["SURVEY_YEAR"] == baseline_year)
        ]["GR_TOTAL_ALL"].sum()
        
        if count > 0:
            funnel_data.append({
                "Stage": display_name,
                "Count": count,
                "Label": f"{int(count):,}"
            })

    if not funnel_data:
        return px.bar(title="No data available")

    # Create funnel chart
    df_plot = pd.DataFrame(funnel_data)
    fig = px.bar(
        df_plot,
        y="Stage",
        x="Count",
        text="Label",
        orientation="h",
        title=f"{selected_institution} Graduation Headcount Funnel of Bachelor's {selected_year-6} Cohort",
        color="Stage",
        color_discrete_sequence=px.colors.sequential.Blues[7::-1]
    )

    fig.update_traces(
        textposition="inside",
        marker_line_color="white",
        marker_line_width=1
    )

    fig.update_layout(
        height=600,
        showlegend=False,
        xaxis_title="Number of Students",
        yaxis_title="Graduation Status",
        margin=dict(t=80, l=20, r=20, b=20),
    )

    return fig

def plot_graduation_gender(df, selected_institution):
    """
    Create a line chart showing gender graduation rates over time for the selected institution

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter for selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()
    
    if inst_df.empty:
        raise ValueError(f"No data found for institution {selected_institution}")

    # Melt the gender data for plotting
    plot_df = inst_df.melt(
        id_vars=['year', 'institution name'],
        value_vars=['Graduation rate, men', 'Graduation rate, women'],
        var_name='Gender',
        value_name='Graduation Rate'
    )

    # Clean up gender labels
    plot_df['Gender'] = plot_df['Gender'].map({
        'Graduation rate, men': 'Men',
        'Graduation rate, women': 'Women'
    })
    
    # Create line chart
    fig = px.line(
        plot_df,
        x='year',
        y='Graduation Rate',
        color='Gender',
        markers=True,
        title=f"{selected_institution} Graduation Rates by Gender Over Time",
        color_discrete_sequence=px.colors.qualitative.Dark24
    )
    
    fig.update_traces(
        text=plot_df['Graduation Rate'].round(1),
        textposition="top center"
    )
    
    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="Year",
        yaxis_title="Graduation Rate (%)",
        showlegend=True,
        xaxis=dict(
            tickmode='linear',
            tick0=plot_df['year'].min(),
            dtick=1,
            tickformat='d'
        )
    )
    
    return fig

def plot_graduation_ethnicity(df, selected_institution, selected_year):
    """
    Create a bar chart showing graduation rates by ethnicity for the selected institution and year

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter for selected institution and year
    inst_df = df[df['institution name'] == selected_institution]
    year_df = inst_df[inst_df['year'] == int(selected_year)].copy()
    
    if year_df.empty:
        raise ValueError(f"No data found for institution {selected_institution} in year {selected_year}")

    # Extract ethnicity data
    race = {
        'American Indian/Alaska Native': year_df['Graduation rate, American Indian or Alaska Native'].iloc[0],
        'Asian': year_df['Graduation rate, Asian'].iloc[0],
        'Native Hawaiian/Pacific Islander': year_df['Graduation rate, Native Hawaiian or Other Pacific Islander'].iloc[0],
        'Black': year_df['Graduation rate, Black, non-Hispanic'].iloc[0],
        'Hispanic': year_df['Graduation rate, Hispanic'].iloc[0],
        'White': year_df['Graduation rate, White, non-Hispanic'].iloc[0]
    }
    
    # Remove any None values and create DataFrame
    race = {k:v for k,v in race.items() if pd.notna(v)}
    df_plot = pd.DataFrame({
        'Ethnicity': race.keys(),
        'Graduation Rate': race.values()
    })
    
    # Create bar chart
    fig = px.bar(
        df_plot,
        x='Ethnicity',
        y='Graduation Rate',
        title=f"{selected_institution} 6-Year Graduation Rates by Ethnicity ({selected_year})",
        color='Ethnicity',
        color_discrete_sequence=px.colors.sequential.Blues[8::-1]
    )
    
    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="",
        yaxis_title="Graduation Rate (%)",
        xaxis={'tickangle': 45},
        showlegend=False,
        margin=dict(b=100)  # Add bottom margin for rotated labels
    )
    
    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='outside'
    )
    
    return fig



