import plotly.express as px
import pandas as pd

def plot_cohort_graduation_rates_over_time(df, selected_institution=None):
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
