import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from lib.colors import NJIT_COLORS

def plot_admission_yield(df, selected_institution):
    df_filtered = df[df['institution name'] == selected_institution].copy()

    # Ensure numeric year
    df_filtered['year'] = pd.to_numeric(df_filtered['year'], errors='coerce')

    # Keep only needed cols
    cols = {
        'Admissions yield - total': 'Total Yield',
        'Admissions yield - full time': 'Full-time Yield',
        'Admissions yield - part time': 'Part-time Yield'
    }
    keep = ['year'] + list(cols.keys())
    tmp = df_filtered[keep].dropna(how='all')

    # Tidy + sort
    plot_df = (
        tmp.rename(columns=cols)
           .melt(id_vars='year', var_name='Metric', value_name='Rate')
           .sort_values(['Metric', 'year'])
           .rename(columns={'year': 'Year'})
    )

    fig = px.line(
        plot_df, x='Year', y='Rate', color='Metric',
        title='Admission Yield Rates Over Time', 
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.update_layout(
        xaxis_title="Year", yaxis_title="Yield Rate (%)",
        xaxis=dict(tickformat="d"),
        legend=dict(orientation="v", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='top center')

    # Make Total Yield line thicker
    for trace in fig.data:
        if trace.name == "Total Yield":
            trace.line.width = 3
            trace.marker.symbol = "triangle-up"
            trace.marker.size = 11
            
    # Make part-time and full-time yield lines dashed
    for trace in fig.data:
        if trace.name in ["Part-time Yield", "Full-time Yield"]:
            trace.line.dash = 'dash'
    return fig

def plot_admission_selectivity(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution].copy()

    # Ensure numeric year
    df_filtered['year'] = pd.to_numeric(df_filtered['year'], errors='coerce')

    cols = {
        'Percent admitted - total': 'Total',
        # 'Percent admitted - men': 'Men',
        # 'Percent admitted - women': 'Women'
    }
    keep = ['year'] + list(cols.keys())
    tmp = df_filtered[keep].dropna(how='all')

    # Tidy + sort
    plot_df = (
        tmp.rename(columns=cols)
           .melt(id_vars='year', var_name='Metric', value_name='Rate')
           .sort_values(['Metric', 'year'])
           .rename(columns={'year': 'Year'})
    )

    fig = px.line(
        plot_df, x='Year', y='Rate', color='Metric',
        title='Admission Selectivity Rates Over Time', markers=True
    )
    fig.update_layout(
        xaxis_title="Year", yaxis_title="Percent admitted (%)",
        xaxis=dict(tickformat="d"),
        legend=dict(orientation="v", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_traces(texttemplate='%{y:.1f}%', textposition='top center')

    return fig

def plot_admission_headcount(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution]

    # Define metrics to plot
    admission_metrics = {
        'Applicants': 'Applicants total',
        'Admitted': 'Admissions total', 
        'Enrolled': 'Enrolled total'
    }

    # Create data for plotting
    admission_data = []
    for year in df_filtered['year'].unique():
        year_data = df_filtered[df_filtered['year'] == year]
        for stage, column in admission_metrics.items():
            if column in df_filtered.columns:
                value = year_data[column].iloc[0] if not year_data.empty else 0
                admission_data.append({
                    'Year': f"Fall {year}",
                    'Stage': stage,
                    'Count': value
                })

    # Convert to DataFrame
    plot_df = pd.DataFrame(admission_data)

    # Create bar plot
    fig = px.bar(
        plot_df,
        x='Year',
        y='Count',
        color='Stage',
        title=f'Fall Admission Funnel: Applications, Admissions, and Enrollment Headcount',
        barmode='group',
        color_discrete_sequence=px.colors.sequential.Blues[::-2]
    )

    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Number of Students",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(tickformat="d"),  # Force integer ticks for years
        height=500
    )

    # Add value labels on bars
    fig.update_traces(
        texttemplate='%{y:,.0f}',
        textposition='outside'
    )
    return fig

