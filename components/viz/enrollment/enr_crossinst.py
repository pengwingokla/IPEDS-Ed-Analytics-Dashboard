import plotly.express as px
import pandas as pd
from lib.colors import NJIT_COLORS

def plot_enrollment_cross_institution(df, selected_multiple_institutions, selected_year):
    # Filter data for selected year and institutions
    df_filtered = df[
        (df['year'] == selected_year) & 
        (df['institution name'].isin(selected_multiple_institutions))
    ]
    
    # Prepare data for stacked bar chart
    df_plot = df_filtered[[
        'institution name', 
        'Full-time undergraduate enrollment', 
        'Full-time graduate enrollment']]
    
    # Create stacked bar chart
    # Melt the dataframe to get it in the right format for stacking
    df_plot_melted = df_plot.melt(
        id_vars=['institution name'],
        value_vars=['Full-time undergraduate enrollment', 'Full-time graduate enrollment'],
        var_name='Degree Level',
        value_name='Number of Students'
    )

    fig = px.bar(
        df_plot_melted,
        x='institution name',
        y='Number of Students',
        color='Degree Level',
        title=f'Full-time Enrollment by Degree Level ({selected_year})',
        labels={
            'institution name': 'Institution',
            'Degree Level': 'Degree Level'
        },
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]],
        barmode='stack'
    )
    # Add number labels on the bars
    fig.update_traces(
        texttemplate='%{y:,.0f}',
        textposition='auto',
        insidetextanchor='middle'
    )

    # Customize layout
    fig.update_layout(
        template='plotly_white',
        height=500,
        showlegend=True,
    )
    return fig

