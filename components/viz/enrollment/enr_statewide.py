import plotly.express as px
import pandas as pd
from lib.colors import NJIT_COLORS

def plot_ug_enrollment_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot pie chart comparing undergraduate enrollment of selected institution vs total of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['STATE'] == selected_state) & (df['year'] == selected_year)].copy()

    # Calculate enrollments
    selected_enrollment = state_df[state_df['institution name'] == selected_institution]['Undergraduate enrollment'].iloc[0]
    
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_enrollment = other_institutions['Undergraduate enrollment'].sum()

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Institution': [selected_institution, f'Other {selected_state} Institutions'],
        'Undergraduate Enrollment': [selected_enrollment, other_enrollment]
    })

    # Create pie chart
    fig = px.pie(
        plot_df,
        values='Undergraduate Enrollment',
        names='Institution',
        title=f"Undergraduate Enrollment Shares ({selected_year}): Selected School vs Other {selected_state} Institutions",
        color='Institution',
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        textposition='auto',
        texttemplate='%{value:,.0f} (%{percent})'
    )

    fig.update_layout(
        template='plotly_white',
        height=500
    )

    return fig

def plot_gr_enrollment_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot pie chart comparing graduate enrollment of selected institution vs total of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['STATE'] == selected_state) & (df['year'] == selected_year)].copy()

    # Calculate enrollments
    selected_enrollment = state_df[state_df['institution name'] == selected_institution]['Graduate enrollment'].iloc[0]
    
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_enrollment = other_institutions['Graduate enrollment'].sum()

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Institution': [selected_institution, f'Other {selected_state} Institutions'],
        'Graduate Enrollment': [selected_enrollment, other_enrollment]
    })

    # Create pie chart
    fig = px.pie(
        plot_df,
        values='Graduate Enrollment',
        names='Institution',
        title=f"Graduate Enrollment Shares ({selected_year}): {selected_institution} vs Other {selected_state} Institutions",
        color='Institution',
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        textposition='auto',
        texttemplate='%{value:,.0f} (%{percent})'
    )

    fig.update_layout(
        template='plotly_white',
        height=500
    )

    return fig

def plot_international_ug_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time international undergraduates of selected institution 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['STATE'] == selected_state) & (df['year'] == selected_year)].copy()

    # Get selected institution's percentage
    selected_pct = state_df[state_df['institution name'] == selected_institution]['Percent of first-time undergraduates - foreign countries'].iloc[0]

    # Calculate mean percentage for other institutions
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_mean_pct = other_institutions['Percent of first-time undergraduates - foreign countries'].mean()

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Institution': [selected_institution, f'Average of Other {selected_state} Institutions'],
        'International Student Percentage': [selected_pct, other_mean_pct]
    })

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='International Student Percentage',
        title=f"International Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='auto'
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        yaxis_title="Percentage of First-Time Undergraduate Students",
        showlegend=False
    )

    return fig


def plot_instate_ug_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time in-state undergraduates of selected institution 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['STATE'] == selected_state) & (df['year'] == selected_year)].copy()

    # Get selected institution's percentage
    selected_pct = state_df[state_df['institution name'] == selected_institution]['Percent of first-time undergraduates - in-state'].iloc[0]

    # Calculate mean percentage for other institutions
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_mean_pct = other_institutions['Percent of first-time undergraduates - in-state'].mean()

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Institution': [selected_institution, f'Average of Other {selected_state} Institutions'],
        'In-State Student Percentage': [selected_pct, other_mean_pct]
    })

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='In-State Student Percentage',
        title=f"In-State Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='auto'
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        yaxis_title="Percentage of First-Time Undergraduate Students",
        showlegend=False
    )

    return fig

def plot_outstate_ug_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time out-of-state undergraduates of selected institution 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['STATE'] == selected_state) & (df['year'] == selected_year)].copy()

    # Get selected institution's percentage
    selected_pct = state_df[state_df['institution name'] == selected_institution]['Percent of first-time undergraduates - out-of-state'].iloc[0]

    # Calculate mean percentage for other institutions
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_mean_pct = other_institutions['Percent of first-time undergraduates - out-of-state'].mean()

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Institution': [selected_institution, f'Average of Other {selected_state} Institutions'],
        'Out-of-State Student Percentage': [selected_pct, other_mean_pct]
    })

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='Out-of-State Student Percentage',
        title=f"Out-of-State Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='auto'
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        yaxis_title="Percentage of First-Time Undergraduate Students",
        showlegend=False
    )

    return fig

def plot_women_ug_statewide(df, selected_institution, selected_state, selected_year):
    """
    Plot line chart comparing percentage of women enrollment (undergraduate and graduate) of selected institution 
    vs average of other institutions in the state over time.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state
    state_df = df[df['STATE'] == selected_state].copy()

    # Get selected institution's percentages over time
    selected_data = state_df[state_df['institution name'] == selected_institution]
    selected_data = selected_data[['year', 
                                 'Percent of undergraduate enrollment that are women',
                                 'Percent of graduate enrollment that are women']]
    selected_data = selected_data.rename(columns={
        'Percent of undergraduate enrollment that are women': 'Selected Institution (Undergraduate)',
        'Percent of graduate enrollment that are women': 'Selected Institution (Graduate)'
    })

    # Calculate mean percentages for other institutions over time
    other_institutions = state_df[state_df['institution name'] != selected_institution]
    other_means = other_institutions.groupby('year').agg({
        'Percent of undergraduate enrollment that are women': 'mean',
        'Percent of graduate enrollment that are women': 'mean'
    }).reset_index()
    other_means = other_means.rename(columns={
        'Percent of undergraduate enrollment that are women': 'State Average (Undergraduate)',
        'Percent of graduate enrollment that are women': 'State Average (Graduate)'
    })

    # Create plot dataframe
    plot_df = pd.merge(selected_data, other_means, on='year', how='outer')
    plot_df = plot_df.melt(id_vars=['year'], 
                          value_vars=['Selected Institution (Undergraduate)', 
                                    'Selected Institution (Graduate)',
                                    'State Average (Undergraduate)',
                                    'State Average (Graduate)'],
                          var_name='Category', 
                          value_name='Percentage')

    # Create line chart
    fig = px.line(
        plot_df,
        x='year',
        y='Percentage',
        color='Category',
        title=f"Women Enrollment Trends in {selected_state}",
        color_discrete_sequence=[NJIT_COLORS["red"], 
                               NJIT_COLORS["navy"], 
                               NJIT_COLORS["red"],
                               NJIT_COLORS["navy"]]
    )

    # Add markers
    fig.update_traces(mode='lines+markers')

    # Make undergraduate lines solid and graduate lines dashed
    for trace in fig.data:
        if "Selected Institution" in trace.name:
            trace.line.dash = 'dash'

    # Customize layout
    fig.update_layout(
        template='plotly_white',
        height=500,
        yaxis_title="Percentage of Students",
        xaxis_title="Year",
        hovermode='x unified'
    )

    # Update y-axis to show percentages and x-axis to show discrete years
    fig.update_yaxes(tickformat='.1f')
    fig.update_xaxes(tickmode='linear', dtick=1)

    return fig




