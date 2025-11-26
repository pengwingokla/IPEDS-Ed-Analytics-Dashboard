import plotly.express as px
import pandas as pd
from lib.colors import NJIT_COLORS

def plot_ug_enrollment_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot pie chart comparing undergraduate enrollment of selected institutions vs total of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['State'] == selected_state) & (df['year'] == selected_year)].copy()

    # Initialize variables
    other_enrollment = 0
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Return empty plot or plot with all as "Other"
        plot_df = pd.DataFrame({
            'Institution': [f'All {selected_state} Institutions'],
            'Undergraduate Enrollment': [state_df['Undergraduate enrollment'].sum()]
        })
    else:
        # Calculate enrollments for selected institutions
        selected_data = []
        for inst in selected_institutions:
            inst_enrollment = state_df[state_df['institution name'] == inst]['Undergraduate enrollment'].iloc[0]
            selected_data.append({'Institution': inst, 'Undergraduate Enrollment': inst_enrollment})
        
        # Calculate enrollment for other institutions
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_enrollment = other_institutions['Undergraduate enrollment'].sum()
        
        # Create plot dataframe
        plot_df = pd.DataFrame(selected_data)
        if other_enrollment > 0:
            plot_df = pd.concat([
                plot_df,
                pd.DataFrame({
                    'Institution': [f'Other {selected_state} Institutions'],
                    'Undergraduate Enrollment': [other_enrollment]
                })
            ], ignore_index=True)

    # Create color sequence - use Plotly Reds palette for selected institutions, navy for others
    if n_selected > 0:
        # Use Plotly's Reds sequential palette, selecting darker shades for better visibility
        # Reverse to get darker reds first, then take the number needed
        reds_palette = px.colors.sequential.Reds[::-1]  # Reverse to get darker shades first
        color_sequence = reds_palette[:n_selected]
    else:
        color_sequence = []
    
    if other_enrollment > 0:
        color_sequence.append(NJIT_COLORS["navy"])

    # Create pie chart
    if n_selected == 0:
        title = f"Undergraduate Enrollment Shares ({selected_year}): All {selected_state} Institutions"
    elif n_selected == 1:
        title = f"Undergraduate Enrollment Shares ({selected_year}): Selected School vs Other {selected_state} Institutions"
    else:
        title = f"Undergraduate Enrollment Shares ({selected_year}): Selected Schools vs Other {selected_state} Institutions"
    
    fig = px.pie(
        plot_df,
        values='Undergraduate Enrollment',
        names='Institution',
        title=title,
        color='Institution',
        color_discrete_sequence=color_sequence if color_sequence else [NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        textposition='auto',
        texttemplate='%{percent}'
    )

    fig.update_layout(
        template='plotly_white',
        height=500
    )

    return fig

def plot_gr_enrollment_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot pie chart comparing graduate enrollment of selected institutions vs total of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['State'] == selected_state) & (df['year'] == selected_year)].copy()

    # Initialize variables
    other_enrollment = 0
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Return empty plot or plot with all as "Other"
        plot_df = pd.DataFrame({
            'Institution': [f'All {selected_state} Institutions'],
            'Graduate Enrollment': [state_df['Graduate enrollment'].sum()]
        })
    else:
        # Calculate enrollments for selected institutions
        selected_data = []
        for inst in selected_institutions:
            inst_enrollment = state_df[state_df['institution name'] == inst]['Graduate enrollment'].iloc[0]
            selected_data.append({'Institution': inst, 'Graduate Enrollment': inst_enrollment})
        
        # Calculate enrollment for other institutions
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_enrollment = other_institutions['Graduate enrollment'].sum()
        
        # Create plot dataframe
        plot_df = pd.DataFrame(selected_data)
        if other_enrollment > 0:
            plot_df = pd.concat([
                plot_df,
                pd.DataFrame({
                    'Institution': [f'Other {selected_state} Institutions'],
                    'Graduate Enrollment': [other_enrollment]
                })
            ], ignore_index=True)

    # Create color sequence - use Plotly Reds palette for selected institutions, navy for others
    if n_selected > 0:
        reds_palette = px.colors.sequential.Reds[::-1]
        color_sequence = reds_palette[:n_selected]
    else:
        color_sequence = []
    
    if other_enrollment > 0:
        color_sequence.append(NJIT_COLORS["navy"])

    # Create pie chart
    if n_selected == 0:
        title = f"Graduate Enrollment Shares ({selected_year}): All {selected_state} Institutions"
    elif n_selected == 1:
        title = f"Graduate Enrollment Shares ({selected_year}): Selected School vs Other {selected_state} Institutions"
    else:
        title = f"Graduate Enrollment Shares ({selected_year}): Selected Schools vs Other {selected_state} Institutions"

    fig = px.pie(
        plot_df,
        values='Graduate Enrollment',
        names='Institution',
        title=title,
        color='Institution',
        color_discrete_sequence=color_sequence if color_sequence else [NJIT_COLORS["navy"]]
    )

    fig.update_traces(
        textposition='auto',
        texttemplate='%{percent}'
    )

    fig.update_layout(
        template='plotly_white',
        height=500
    )

    return fig

def plot_international_ug_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time international undergraduates of selected institutions 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['State'] == selected_state) & (df['year'] == selected_year)].copy()

    # Initialize variables
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Show average of all institutions
        all_mean_pct = state_df['Percent of first-time undergraduates - foreign countries'].mean()
        plot_df = pd.DataFrame({
            'Institution': [f'Average of All {selected_state} Institutions'],
            'International Student Percentage': [all_mean_pct]
        })
        color_sequence = [NJIT_COLORS["navy"]]
    else:
        # Get selected institutions' percentages
        selected_data = []
        for inst in selected_institutions:
            inst_pct = state_df[state_df['institution name'] == inst]['Percent of first-time undergraduates - foreign countries'].iloc[0]
            selected_data.append({'Institution': inst, 'International Student Percentage': inst_pct})
        
        # Calculate mean percentage for other institutions
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_mean_pct = other_institutions['Percent of first-time undergraduates - foreign countries'].mean()
        
        # Create plot dataframe
        plot_df = pd.DataFrame(selected_data)
        if len(other_institutions) > 0:
            plot_df = pd.concat([
                plot_df,
                pd.DataFrame({
                    'Institution': [f'Average of Other {selected_state} Institutions'],
                    'International Student Percentage': [other_mean_pct]
                })
            ], ignore_index=True)
        
        # Create color sequence - use Plotly Reds palette for selected institutions, navy for others
        reds_palette = px.colors.sequential.Reds[::-1]
        color_sequence = reds_palette[:n_selected]
        if len(other_institutions) > 0:
            color_sequence.append(NJIT_COLORS["navy"])

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='International Student Percentage',
        title=f"International Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=color_sequence
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


def plot_instate_ug_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time in-state undergraduates of selected institutions 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['State'] == selected_state) & (df['year'] == selected_year)].copy()

    # Initialize variables
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Show average of all institutions
        all_mean_pct = state_df['Percent of first-time undergraduates - in-state'].mean()
        plot_df = pd.DataFrame({
            'Institution': [f'Average of All {selected_state} Institutions'],
            'In-State Student Percentage': [all_mean_pct]
        })
        color_sequence = [NJIT_COLORS["navy"]]
    else:
        # Get selected institutions' percentages
        selected_data = []
        for inst in selected_institutions:
            inst_pct = state_df[state_df['institution name'] == inst]['Percent of first-time undergraduates - in-state'].iloc[0]
            selected_data.append({'Institution': inst, 'In-State Student Percentage': inst_pct})
        
        # Calculate mean percentage for other institutions
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_mean_pct = other_institutions['Percent of first-time undergraduates - in-state'].mean()
        
        # Create plot dataframe
        plot_df = pd.DataFrame(selected_data)
        if len(other_institutions) > 0:
            plot_df = pd.concat([
                plot_df,
                pd.DataFrame({
                    'Institution': [f'Average of Other {selected_state} Institutions'],
                    'In-State Student Percentage': [other_mean_pct]
                })
            ], ignore_index=True)
        
        # Create color sequence - use Plotly Reds palette for selected institutions, navy for others
        reds_palette = px.colors.sequential.Reds[::-1]
        color_sequence = reds_palette[:n_selected]
        if len(other_institutions) > 0:
            color_sequence.append(NJIT_COLORS["navy"])

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='In-State Student Percentage',
        title=f"In-State Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=color_sequence
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

def plot_outstate_ug_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot bar chart comparing percentage of first-time out-of-state undergraduates of selected institutions 
    vs average of other institutions in the state.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state and year
    state_df = df[(df['State'] == selected_state) & (df['year'] == selected_year)].copy()

    # Initialize variables
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Show average of all institutions
        all_mean_pct = state_df['Percent of first-time undergraduates - out-of-state'].mean()
        plot_df = pd.DataFrame({
            'Institution': [f'Average of All {selected_state} Institutions'],
            'Out-of-State Student Percentage': [all_mean_pct]
        })
        color_sequence = [NJIT_COLORS["navy"]]
    else:
        # Get selected institutions' percentages
        selected_data = []
        for inst in selected_institutions:
            inst_pct = state_df[state_df['institution name'] == inst]['Percent of first-time undergraduates - out-of-state'].iloc[0]
            selected_data.append({'Institution': inst, 'Out-of-State Student Percentage': inst_pct})
        
        # Calculate mean percentage for other institutions
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_mean_pct = other_institutions['Percent of first-time undergraduates - out-of-state'].mean()
        
        # Create plot dataframe
        plot_df = pd.DataFrame(selected_data)
        if len(other_institutions) > 0:
            plot_df = pd.concat([
                plot_df,
                pd.DataFrame({
                    'Institution': [f'Average of Other {selected_state} Institutions'],
                    'Out-of-State Student Percentage': [other_mean_pct]
                })
            ], ignore_index=True)
        
        # Create color sequence - use Plotly Reds palette for selected institutions, navy for others
        reds_palette = px.colors.sequential.Reds[::-1]
        color_sequence = reds_palette[:n_selected]
        if len(other_institutions) > 0:
            color_sequence.append(NJIT_COLORS["navy"])

    # Create bar chart
    fig = px.bar(
        plot_df,
        x='Institution',
        y='Out-of-State Student Percentage',
        title=f"Out-of-State Undergraduate Students ({selected_year})",
        color='Institution',
        color_discrete_sequence=color_sequence
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

def plot_women_ug_statewide(df, selected_institutions, selected_state, selected_year):
    """
    Plot line chart comparing percentage of women enrollment (undergraduate and graduate) of selected institutions 
    vs average of other institutions in the state over time.

    Notes
    -----
    Hugging Face source: `chloecodes/IPEDS_CUSTOM`
    """
    # Filter data for the selected state
    state_df = df[df['State'] == selected_state].copy()

    # Initialize variables
    n_selected = len(selected_institutions) if selected_institutions else 0

    # Handle case when no institutions are selected
    if not selected_institutions or len(selected_institutions) == 0:
        # Show only state average
        other_institutions = state_df
        other_means = other_institutions.groupby('year').agg({
            'Percent of undergraduate enrollment that are women': 'mean',
            'Percent of graduate enrollment that are women': 'mean'
        }).reset_index()
        other_means = other_means.rename(columns={
            'Percent of undergraduate enrollment that are women': 'State Average (Undergraduate)',
            'Percent of graduate enrollment that are women': 'State Average (Graduate)'
        })
        plot_df = other_means.melt(id_vars=['year'], 
                                  value_vars=['State Average (Undergraduate)',
                                            'State Average (Graduate)'],
                                  var_name='Category', 
                                  value_name='Percentage')
        color_map = {
            'State Average (Undergraduate)': NJIT_COLORS["navy"],
            'State Average (Graduate)': NJIT_COLORS["navy"]
        }
    else:
        # Get selected institutions' percentages over time
        all_selected_data = []
        for inst in selected_institutions:
            inst_data = state_df[state_df['institution name'] == inst]
            inst_data = inst_data[['year', 
                                 'Percent of undergraduate enrollment that are women',
                                 'Percent of graduate enrollment that are women']].copy()
            inst_data = inst_data.rename(columns={
                'Percent of undergraduate enrollment that are women': f'{inst} (Undergraduate)',
                'Percent of graduate enrollment that are women': f'{inst} (Graduate)'
            })
            all_selected_data.append(inst_data)

        # Merge all selected institutions
        if len(all_selected_data) > 1:
            selected_merged = all_selected_data[0]
            for inst_data in all_selected_data[1:]:
                selected_merged = pd.merge(selected_merged, inst_data, on='year', how='outer')
        else:
            selected_merged = all_selected_data[0]

        # Calculate mean percentages for other institutions over time
        other_institutions = state_df[~state_df['institution name'].isin(selected_institutions)]
        other_means = other_institutions.groupby('year').agg({
            'Percent of undergraduate enrollment that are women': 'mean',
            'Percent of graduate enrollment that are women': 'mean'
        }).reset_index()
        other_means = other_means.rename(columns={
            'Percent of undergraduate enrollment that are women': 'State Average (Undergraduate)',
            'Percent of graduate enrollment that are women': 'State Average (Graduate)'
        })

        # Create plot dataframe
        plot_df = pd.merge(selected_merged, other_means, on='year', how='outer')
        
        # Get column names for melting
        value_vars = [col for col in plot_df.columns if col != 'year']
        plot_df = plot_df.melt(id_vars=['year'], 
                              value_vars=value_vars,
                              var_name='Category', 
                              value_name='Percentage')

        # Create color map - use Plotly Reds palette for selected institutions, navy for state average
        reds_palette = px.colors.sequential.Reds[::-1]
        color_map = {}
        
        # Assign red shades to selected institutions (each has UG and Grad)
        for i, inst in enumerate(selected_institutions):
            red_color = reds_palette[i] if i < len(reds_palette) else reds_palette[-1]
            color_map[f'{inst} (Undergraduate)'] = red_color
            color_map[f'{inst} (Graduate)'] = red_color
        
        # Add navy for state average (UG and Grad)
        if len(other_institutions) > 0:
            color_map['State Average (Undergraduate)'] = NJIT_COLORS["navy"]
            color_map['State Average (Graduate)'] = NJIT_COLORS["navy"]

    # Create line chart
    fig = px.line(
        plot_df,
        x='year',
        y='Percentage',
        color='Category',
        title=f"Women Enrollment Trends in {selected_state}",
        color_discrete_map=color_map
    )

    # Add markers
    fig.update_traces(mode='lines+markers')

    # Make graduate lines dashed
    for trace in fig.data:
        if "(Graduate)" in trace.name:
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




