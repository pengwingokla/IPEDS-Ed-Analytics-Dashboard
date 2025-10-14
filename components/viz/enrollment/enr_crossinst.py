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
        'Undergraduate enrollment', 
        'Graduate enrollment']]
    
    # Create stacked bar chart
    # Melt the dataframe to get it in the right format for stacking
    df_plot_melted = df_plot.melt(
        id_vars=['institution name'],
        value_vars=['Undergraduate enrollment', 'Graduate enrollment'],
        var_name='Degree Level',
        value_name='Number of Students'
    )

    fig = px.bar(
        df_plot_melted,
        x='institution name',
        y='Number of Students',
        color='Degree Level',
        title=f'Enrollment Headcount by Degree Level ({selected_year})',
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

def plot_ugenrollment_age_distribution_cross_institution(df, selected_multiple_institutions, selected_year):
    # Filter data for selected year and institutions
    df_filtered = df[
        (df['year'] == selected_year) & 
        (df['institution name'].isin(selected_multiple_institutions))
    ]
    
    # Prepare data for stacked bar chart
    df_plot = pd.DataFrame({
        'institution name': df_filtered['institution name'],
        'Under 18': df_filtered['Percent of undergraduate enrollment under 18'],
        '18-24': df_filtered['Percent of undergraduate enrollment 18-24'],
        '25-64': df_filtered['Percent of undergraduate enrollment, 25-64'], 
        'Over 65': df_filtered['Percent of undergraduate enrollment over 65']
    })
    
    # Create stacked bar chart
    # Melt the dataframe to get it in the right format for stacking
    df_plot_melted = df_plot.melt(
        id_vars=['institution name'],
        value_vars=[
            'Under 18',
            '18-24', 
            '25-64',
            'Over 65'
        ],
        var_name='Age Group',
        value_name='Percentage'
    )

    fig = px.bar(
        df_plot_melted,
        x='institution name',
        y='Percentage',
        color='Age Group',
        title=f'Undergraduate Enrollment by Age Group ({selected_year})',
        labels={
            'institution name': 'Institution',
            'Percentage': 'Percentage of Students',
            'Age Group': 'Age Group'
        },
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"], NJIT_COLORS["gray"], NJIT_COLORS["black"]],
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

def plot_ugenrollment_residence_cross_institution(df, selected_multiple_institutions, selected_year):
    # Filter data for selected year and institutions
    df_filtered = df[
        (df['year'] == selected_year) & 
        (df['institution name'].isin(selected_multiple_institutions))
    ]
    
    # Prepare data for grouped bar chart
    df_plot = pd.DataFrame({
        'institution name': df_filtered['institution name'],
        'In-State': df_filtered['Percent of first-time undergraduates - in-state'],
        'Out-of-State': df_filtered['Percent of first-time undergraduates - out-of-state'],
        'Foreign Countries': df_filtered['Percent of first-time undergraduates - foreign countries'], 
        'Unknown': df_filtered['Percent of first-time undergraduates - residence unknown']
    })
    
    # Melt the dataframe to get it in the right format for grouping
    df_plot_melted = df_plot.melt(
        id_vars=['institution name'],
        value_vars=[
            'In-State',
            'Out-of-State', 
            'Foreign Countries',
            'Unknown'
        ],
        var_name='Residence',
        value_name='Percentage'
    )

    fig = px.bar(
        df_plot_melted,
        x='institution name',
        y='Percentage',
        color='Residence',
        title=f'Undergraduate Enrollment by Residence ({selected_year})',
        labels={
            'institution name': 'Institution',
            'Percentage': 'Percentage of Students',
            'Residence': 'Residence'
        },
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"], NJIT_COLORS["gray"], NJIT_COLORS["black"]],
        barmode='group'  # Changed from 'stack' to 'group'
    )
    # Add number labels on the bars
    fig.update_traces(
        texttemplate='%{y:.1f}%',  # Changed to show percentage with 1 decimal place
        textposition='auto',
        insidetextanchor='middle'
    )

    # Customize layout
    fig.update_layout(
        template='plotly_white',
        height=500,
        showlegend=True,
        yaxis_range=[0, 100]  # Set y-axis range from 0 to 100 since showing percentages
    )
    return fig