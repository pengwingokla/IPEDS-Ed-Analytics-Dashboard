import plotly.express as px
import pandas as pd
from lib.colors import NJIT_COLORS

def plot_ugenrollment_headcount(df, selected_institution):
    """
    Create a stacked bar chart showing undergraduate and graduate enrollment trends over time for the selected institution

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter for selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()
    
    if inst_df.empty:
        raise ValueError(f"No data found for institution {selected_institution}")

    # Create plot dataframe with both undergraduate and graduate enrollment
    plot_df = pd.DataFrame({
        'Year': pd.concat([inst_df['year'], inst_df['year']]).reset_index(drop=True),
        'Enrollment': pd.concat([
            inst_df['Undergraduate enrollment'],
            inst_df['Graduate enrollment']
        ]).reset_index(drop=True),
        'Degree Level': ['Undergraduate'] * len(inst_df) + ['Graduate'] * len(inst_df)
    })

    # Create stacked bar chart
    fig = px.bar(
        plot_df,
        x='Year',
        y='Enrollment',
        color='Degree Level',
        title=f"{selected_institution} Enrollment Trends by Degree Level",
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]],
        text=plot_df['Enrollment'].round(0).astype(int)
    )

    fig.update_traces(
        textposition="auto",
        marker_line_width=0  # Remove the white border around bars
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="Year",
        yaxis_title="Total Enrollment",
        xaxis=dict(
            tickmode='linear',
            tick0=plot_df['Year'].min(),
            dtick=1,
            tickformat='d'
        ),
        yaxis=dict(
            tickformat=',d'
        ),
        legend=dict(
            yanchor="top",
            xanchor="left",
        ),
        barmode='stack'
    )

    return fig

def plot_ugenrollment_age_distribution(df, selected_institution=None):
    """
    Plot percentage distribution of undergraduate enrollment by age group for a selected institution.

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

    # Create plot dataframe with age distribution columns
    plot_df = pd.DataFrame({
        'Year': inst_df['year'],
        'Under 18': inst_df['Percent of undergraduate enrollment under 18'],
        '18-24': inst_df['Percent of undergraduate enrollment 18-24'],
        '25-64': inst_df['Percent of undergraduate enrollment, 25-64'],
        'Over 65': inst_df['Percent of undergraduate enrollment over 65']
    })

    # Melt the dataframe for plotting
    plot_df = plot_df.melt(
        id_vars=['Year'],
        value_vars=['Under 18', '18-24', '25-64', 'Over 65'],
        var_name='Age Group',
        value_name='Percentage'
    )
    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Year',
        y='Percentage',
        color='Age Group',
        title=f"{selected_institution} Undergraduate Enrollment by Age Group",
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"], NJIT_COLORS["gray"], NJIT_COLORS["black"]],
        text=plot_df['Percentage'].round(1).astype(str) + '%'
    )

    fig.update_traces(
        textposition="auto",
        marker_line_width=0
    )

    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="Year",
        yaxis_title="Percentage of Enrollment",
        xaxis=dict(
            tickmode='linear',
            tick0=plot_df['Year'].min(),
            dtick=1,
            tickformat='d'
        ),
        yaxis=dict(
            tickformat='.1f',
            ticksuffix='%'
        ),
        legend=dict(
            yanchor="top",
            xanchor="right",
        ),
        barmode='stack'
    )

    return fig

def plot_ugenrollment_gender(df, selected_institution):
    """
    Plot percentage of undergraduate enrollment that are women over time.

    Parameters
    ----------
    df : pandas.DataFrame
        The input dataframe containing enrollment data
    selected_institution : str
        Name of the selected institution to plot data for

    Returns
    -------
    plotly.graph_objects.Figure
        The plotly figure object containing the line plot
    """
    # Filter for selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()

    if inst_df.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Year': inst_df['year'],
        'Undergraduate Women': inst_df['Percent of undergraduate enrollment that are women'],
        'Graduate Women': inst_df['Percent of graduate enrollment that are women']
    })
    # Create line plot
    fig = px.line(
        plot_df,
        x='Year',
        y=['Undergraduate Women', 'Graduate Women'],
        title=f"{selected_institution} Share of Women in Enrollment",
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]],
        markers=True
    )

    # Update layout
    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="Year",
        yaxis_title="Percentage of Women (%)",
        xaxis=dict(
            tickmode='linear',
            tick0=plot_df['Year'].min(),
            dtick=1,
            tickformat='d'
        ),
        yaxis=dict(
            tickformat='.1f',
            ticksuffix='%'
        ),
        legend_title=None
    )

    # Add value labels on points
    fig.update_traces(
        text=plot_df['Undergraduate Women'].round(1),
        textposition="top center",
        marker_line_width=0
    )

    return fig
def plot_ugenrollment_ft_pt(df, selected_institution):
    """
    Create a grouped bar chart showing full-time and part-time undergraduate enrollment trends over time for the selected institution

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter for selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()
    
    if inst_df.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Create plot dataframe
    plot_df = pd.DataFrame({
        'Year': inst_df['year'],
        'Full-time': inst_df['Full-time undergraduate enrollment'],
        'Part-time': inst_df['Part-time undergraduate enrollment']
    })

    # Create grouped bar chart
    fig = px.bar(
        plot_df,
        x='Year',
        y=['Full-time', 'Part-time'],
        title=f"{selected_institution} Full-Time vs Part-Time Enrollment",
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"]],
        barmode='group'
    )

    # Update layout
    fig.update_layout(
        template='plotly_white',
        height=500,
        xaxis_title="Year",
        yaxis_title="Number of Students",
        xaxis=dict(
            tickmode='linear',
            tick0=plot_df['Year'].min(),
            dtick=1,
            tickformat='d'
        ),
        legend_title=None
    )

    # Add value labels on bars
    fig.update_traces(
        texttemplate='%{y:,.0f}',
        textposition='outside'
    )

    return fig

def plot_ugenrollment_race(df, selected_institution=None, selected_year=None):
    """
    Create a horizontal bar chart showing undergraduate enrollment percentages by race/ethnicity
    
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

    # Get the year data
    if selected_year is not None:
        if selected_year not in inst_df['year'].values:
            raise ValueError(f"Selected year {selected_year} not found in data for {selected_institution}")
    else:
        selected_year = inst_df['year'].max()
    data = inst_df[inst_df['year'] == selected_year].iloc[0]

    # Create dataframe with enrollment percentages by race/ethnicity
    enrollment_data = {
        'Ethnicity': [
            'Asian',
            'Asian/Native Hawaiian/Pacific Islander',
            'Black or African American',
            'Hispanic/Latino',
            'Native Hawaiian or Other Pacific Islander',
            'White',
            # 'Two or More Races',
            'Unknown',
            # 'U.S. Nonresident'
        ],
        'Percentage': [
            data['Percent of undergraduate enrollment that are Asian'],
            data['Percent of undergraduate enrollment that are Asian/Native Hawaiian/Pacific Islander'],
            data['Percent of undergraduate enrollment that are Black or African American'],
            data['Percent of undergraduate enrollment that are Hispanic/Latino'],
            data['Percent of undergraduate enrollment that are Native Hawaiian or Other Pacific Islander'],
            data['Percent of undergraduate enrollment that are White'],
            # data['Percent of undergraduate enrollment that are two or more races'],
            data['Percent of undergraduate enrollment that are Race/ethnicity unknown'],
            # data['Percent of undergraduate enrollment that are U.S. Nonresident']
        ]
    }
    plot_df = pd.DataFrame(enrollment_data)
    
    # Sort dataframe by percentage in descending order
    plot_df = plot_df.sort_values('Percentage', ascending=False)

    # Create horizontal bar chart
    fig = px.bar(
        plot_df,
        y='Ethnicity',
        x='Percentage',
        orientation='h',
        text=plot_df['Percentage'],
        title=f"{selected_institution} Undergraduate Enrollment by Ethnicity ({selected_year})",
        color='Ethnicity',
        color_discrete_sequence=px.colors.sequential.Greys[2:],  # Current: Blue shades
    )

    # Update layout
    fig.update_layout(
        template='plotly_white',
        height=600,  # Increased height to accommodate more categories
        xaxis_title="Percentage of Total Enrollment",
        yaxis_title=None,
        showlegend=False
    )

    # Add percentage labels on bars
    fig.update_traces(
        texttemplate='%{x:.1f}%',
        textposition='auto',
        marker_line_width=0
    )

    return fig

def plot_ugenrollment_residence(df, selected_institution, selected_year):
    # Default to NJIT if no institution is selected
    if selected_institution is None:
        selected_institution = 'New Jersey Institute of Technology'
    
    # Filter data for the selected institution
    inst_df = df[df['institution name'] == selected_institution].copy()

    if inst_df.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Get the most recent year's data
    if selected_year is not None:
        if selected_year not in inst_df['year'].values:
            raise ValueError(f"Selected year {selected_year} not found in data for {selected_institution}")
    else:
        selected_year = inst_df['year'].max()
    data = inst_df[inst_df['year'] == selected_year].iloc[0]

    # Prepare data for plotting
    enrollment_data = {
        'Residence': [
            'In-State',
            'Out-of-State', 
            'Foreign Countries',
            'Unknown'
        ],
        'Percentage': [
            data['Percent of first-time undergraduates - in-state'],
            data['Percent of first-time undergraduates - out-of-state'],
            data['Percent of first-time undergraduates - foreign countries'],
            data['Percent of first-time undergraduates - residence unknown']
        ]
    }
    plot_df = pd.DataFrame(enrollment_data)

    # Create pie chart
    fig = px.pie(
        plot_df,
        values='Percentage',
        names='Residence',
        title=f"{selected_institution} First-Time Undergraduate Enrollment by Residence ({selected_year})",
        color_discrete_sequence=[NJIT_COLORS["red"], NJIT_COLORS["navy"], NJIT_COLORS["gray"], NJIT_COLORS["white"]]
    )

    # Update layout
    fig.update_layout(
        template='plotly_white',
        showlegend=True,
        height=600,
        width=None
    )

    # Update traces
    fig.update_traces(
        textposition='inside',
        textinfo='percent+value',
        marker_line_width=0,
        texttemplate='%{percent}'
    )

    return fig

