import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from lib.colors import NJIT_COLORS

def plot_aid_type_stackedbar(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution]
    
    # Prepare the data for the stacked bar chart
    aid_categories = {
        'Federal Grant Aid': 'Percent of full-time first-time undergraduates awarded federal grant aid',
        'State/Local Grant Aid': 'Percent of full-time first-time undergraduates awarded state/local grant aid',
        'Institutional Grant Aid': 'Percent of full-time first-time undergraduates awarded institutional grant aid',
        'Pell Grants': 'Percent of full-time first-time undergraduates awarded Pell grants',
        'Other Federal Grant Aid': 'Percent of full-time first-time undergraduates awarded other federal grant aid'
    }
    
    # Create long format dataframe for plotting
    aid_data = []
    for category, column in aid_categories.items():
        data = df_filtered[['year', column]].copy()
        data['Category'] = category
        data['Percentage'] = data[column]
        aid_data.append(data[['year', 'Category', 'Percentage']])
    
    aid_df = pd.concat(aid_data)
    
    # Create stacked bar chart
    fig = px.bar(
        aid_df,
        x='year',
        y='Percentage',
        color='Category',
        title=f'Financial Aid Distribution Over Time',
        color_discrete_sequence=px.colors.sequential.Greens[::-2],
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Percentage",
        barmode='stack',
        showlegend=True,
        legend=dict(
            orientation="v", 
            yanchor="top", 
            y=1, 
            xanchor="left", 
            x=1.02
        )
    )
    
    # Add percentage labels on bars
    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='inside'
    )

    return fig

def plot_aid_received_linechart(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution]
    
    # Define the columns to plot
    aid_metrics = {
        'Any Aid': 'Percent of full-time first-time undergraduates awarded any loans to students or grant aid  from federal state/local government or the institution',
        'Grant Only': 'Percent of full-time first-time undergraduates awarded federal, state, local or institutional grant aid'
    }
    
    # Create long format dataframe for plotting
    aid_data = []
    for metric, column in aid_metrics.items():
        data = df_filtered[['year', column]].copy()
        data['Metric'] = metric
        data['Percentage'] = data[column]
        aid_data.append(data[['year', 'Metric', 'Percentage']])
    
    aid_df = pd.concat(aid_data)
    
    # Create line plot
    fig = px.line(
        aid_df,  # Changed from aid_data to aid_df
        x='year',
        y='Percentage',
        color='Metric',
        title=f'Percentage of Students Received Financial Aid',
        markers=True,
        color_discrete_sequence=['#2ca02c', '#ff7f0e']
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Percentage of Students",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis=dict(tickformat="d") # Force integer ticks for years
    )
    
    # Add percentage labels on points
    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='top center'
    )

    return fig

def plot_total_aid_disbursed_linechart(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution]
    
    aid_metrics = {
        # 'Federal Grant Aid': 'Total amount of federal grant aid awarded to full-time first-time undergraduates',
        # 'Pell Grant Aid': 'Total amount of Pell grant aid awarded to full-time first-time undergraduates',
        # 'Institutional Grant Aid': 'Total amount of institutional grant aid awarded to full-time first-time undergraduates',
        # 'State/Local Grant Aid': 'Total amount of state/local grant aid awarded to full-time first-time undergraduates',
        'Other Federal Grant Aid': 'Total amount of other federal grant aid awarded to full-time first-time undergraduates',
        'Total Grant Aid (FTFT)': 'Total amount of federal, state, local or institutional grant aid awarded to full-time first-time undergraduates',
        # 'Total Grant Aid (All UG)': 'Total amount of federal, state, local, institutional or other sources of grant aid awarded to undergraduate students',
        # 'Federal Student Loans (FTFT)': 'Total amount of federal student loans awarded to full-time first-time undergraduates',
        # 'Other Student Loans (FTFT)': 'Total amount of other student loans awarded to full-time first-time undergraduates',
        'Total Student Loans (FTFT)': 'Total amount of student loans awarded to full-time first-time undergraduates',
        # 'Federal Student Loans (All UG)': 'Total amount of federal student loans awarded to undergraduate students'
    }
    
    # Create data for plotting
    aid_data = []
    for year in df_filtered['year'].unique():
        year_data = df_filtered[df_filtered['year'] == year]
        for metric, column in aid_metrics.items():
            if column in df_filtered.columns:
                value = year_data[column].iloc[0] if not year_data.empty else 0
                aid_data.append({
                    'Year': year,
                    'Aid Type': metric,
                    'Amount': value
                })
    
    # Convert to DataFrame
    plot_df = pd.DataFrame(aid_data)
    
    # Create line plot
    fig = px.line(
        plot_df,
        x='Year',
        y='Amount',
        color='Aid Type',
        title=f'Total Amount of Financial Aid Disbursed Over Time',
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Amount ($)",
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.02),
        height=600
    )
    
    # Format y-axis labels as currency
    fig.update_layout(
        yaxis=dict(tickformat="$,.0f"),
        xaxis=dict(tickformat="d") # Force integer ticks for years
    )
    
    return fig

def plot_tuition_type_pie(df, selected_institution, selected_year):
    # Filter data for selected institution and year
    df = df[(df['year'] == selected_year) & (df['institution name'] == selected_institution)]
    
    # Prepare the data for the pie chart
    tuition_data = {
        'Category': ['In-District', 'In-State', 'Out-of-State', 'Unknown'],
        'Count': [
            df['Percentage of students in fall cohort who are paying in-district tuition rates'].iloc[0],
            df['Percentage of students in fall cohort who paying in-state tuition rates'].iloc[0], 
            df['Percentage of students in fall cohort who are paying out-of-state tuition rates'].iloc[0],
            df['Percentage of students in fall cohort whose residence/ tuition rate is unknown'].iloc[0]
        ]
    }
    tuition_df = pd.DataFrame(tuition_data)
    
    # Create pie chart
    fig = px.pie(
        tuition_df,
        values='Count',
        names='Category',
        title=f'Fall Cohort Tuition Rate Composition',
        color_discrete_sequence=['#2ca02c', '#ff7f0e']
    )
    
    # Update layout
    fig.update_traces(
        textposition='auto',
        textinfo='percent+label'
    )
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5)
    )
    return fig

def plot_category_aid_disbursed(df, selected_institution, selected_year):
    # Filter data for selected institution and year
    df_filtered = df[(df['institution name'] == selected_institution) & (df['year'] == selected_year)]
    
    # Define aid metrics and their corresponding column names
    aid_metrics = {
        'Federal Grant Aid': 'Total amount of federal grant aid awarded to full-time first-time undergraduates',
        'Pell Grants': 'Total amount of Pell grant aid awarded to full-time first-time undergraduates',
        'Institutional Grant Aid': 'Total amount of institutional grant aid awarded to full-time first-time undergraduates',
        'State/Local Grant Aid': 'Total amount of state/local grant aid awarded to full-time first-time undergraduates',
        'Other Federal Grant Aid': 'Total amount of other federal grant aid awarded to full-time first-time undergraduates',
        'Federal Student Loans (FT/FT)': 'Total amount of federal student loans awarded to full-time first-time undergraduates',
        'Other Student Loans (FT/FT)': 'Total amount of other student loans awarded to full-time first-time undergraduates',
        # 'Federal Student Loans (All UG)': 'Total amount of federal student loans awarded to undergraduate students',
        # 'Total Student Loans (FT/FT)': 'Total amount of student loans awarded to full-time first-time undergraduates',
        # 'Total Grant Aid (FT/FT)': 'Total amount of federal, state, local or institutional grant aid awarded to full-time first-time undergraduates',
        # 'Total Grant Aid (All UG)': 'Total amount of federal, state, local, institutional or other sources of grant aid awarded to undergraduate students',
    }
    
    # Create data for plotting
    aid_data = []
    for metric, column in aid_metrics.items():
        if column in df_filtered.columns:
            value = df_filtered[column].iloc[0] if not df_filtered.empty else 0
            aid_data.append({
                'Aid Type': metric,
                'Amount': value
            })
    
    # Convert to DataFrame
    plot_df = pd.DataFrame(aid_data)
    
    # Create bar plot
    fig = px.bar(
        plot_df,
        x='Aid Type',
        y='Amount',
        title=f'Total Financial Aid Disbursed by Type ({selected_year})',
        color='Aid Type',
        color_discrete_sequence=px.colors.sequential.Greens[::-2]
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Aid Type",
        yaxis_title="Amount ($)",
        showlegend=False,
        xaxis_tickangle=45,
        height=600
    )
    
    # Format y-axis labels as currency
    fig.update_layout(
        yaxis=dict(
            tickformat="$,.0f"
        )
    )
    
    # Add value labels on bars
    fig.update_traces(
        texttemplate='$%{y:,.0f}',
        textposition='outside'
    )

    return fig

def plot_total_aid_disbursed(df, selected_institution, selected_year):
    # Filter data for selected institution and year
    df_filtered = df[(df['institution name'] == selected_institution) & (df['year'] == selected_year)]
    
    # Define aid metrics and their corresponding column names
    aid_metrics = {
        # 'Federal Grant Aid': 'Total amount of federal grant aid awarded to full-time first-time undergraduates',
        # 'Pell Grants': 'Total amount of Pell grant aid awarded to full-time first-time undergraduates',
        # 'Institutional Grant Aid': 'Total amount of institutional grant aid awarded to full-time first-time undergraduates',
        # 'State/Local Grant Aid': 'Total amount of state/local grant aid awarded to full-time first-time undergraduates',
        # 'Other Federal Grant Aid': 'Total amount of other federal grant aid awarded to full-time first-time undergraduates',
        # 'Federal Student Loans (FT/FT)': 'Total amount of federal student loans awarded to full-time first-time undergraduates',
        # 'Other Student Loans (FT/FT)': 'Total amount of other student loans awarded to full-time first-time undergraduates',
        # 'Federal Student Loans (All UG)': 'Total amount of federal student loans awarded to undergraduate students',
        'Total Student Loans (FT/FT)': 'Total amount of student loans awarded to full-time first-time undergraduates',
        'Total Grant Aid (FT/FT)': 'Total amount of federal, state, local or institutional grant aid awarded to full-time first-time undergraduates',
        'Total Grant Aid (All UG)': 'Total amount of federal, state, local, institutional or other sources of grant aid awarded to undergraduate students',
    }
    
    # Create data for plotting
    aid_data = []
    for metric, column in aid_metrics.items():
        if column in df_filtered.columns:
            value = df_filtered[column].iloc[0] if not df_filtered.empty else 0
            aid_data.append({
                'Aid Type': metric,
                'Amount': value
            })
    
    # Convert to DataFrame
    plot_df = pd.DataFrame(aid_data)
    
    # Create bar plot
    fig = px.bar(
        plot_df,
        x='Aid Type',
        y='Amount',
        title=f'Type of Aid Disbursed ({selected_year})',
        color='Aid Type',
        color_discrete_sequence=px.colors.sequential.Greens[::-1]
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Aid Type",
        yaxis_title="Amount ($)",
        showlegend=False,
        xaxis_tickangle=45,
        height=600
    )
    
    # Format y-axis labels as currency
    fig.update_layout(
        yaxis=dict(
            tickformat="$,.0f"
        )
    )
    
    # Add value labels on bars
    fig.update_traces(
        texttemplate='$%{y:,.0f}',
        textposition='outside'
    )

    return fig

def plot_student_loan_dualaxis(df, selected_institution):
    # Filter data for selected institution and sort by year
    df_filtered = df[df['institution name'] == selected_institution].copy()
    df_filtered = df_filtered.sort_values('year')

    # Create dataframe for student counts
    students_df = pd.DataFrame({
        'Year': df_filtered['year'].repeat(3),
        'Category': ['Total Student Loans', 'Federal Student Loans', 'Other Student Loans'] * len(df_filtered),
        'Number of Students': [
            *df_filtered['Number of full-time first-time undergraduates awarded student loans'],
            *df_filtered['Number of full-time first-time undergraduates awarded federal student loans'], 
            *df_filtered['Number of full-time first-time undergraduates awarded other student loans']
        ]
    })

    # Create dataframe for average amounts
    amounts_df = pd.DataFrame({
        'Year': df_filtered['year'].repeat(3),
        'Category': ['Average Total', 'Average Federal', 'Average Other'] * len(df_filtered),
        'Average Amount': [
            *df_filtered['Average amount of student loans awarded to full-time first-time undergraduates'],
            *df_filtered['Average amount of federal student loans awarded to full-time first-time undergraduates'],
            *df_filtered['Average amount of other student loans awarded to full-time first-time undergraduates']
        ]
    })

    # Create bar chart for student counts
    fig1 = px.bar(
        students_df,
        x='Year',
        y='Number of Students',
        color='Category',
        barmode='group',
        title=f'Student Loan Analysis',
        color_discrete_sequence=px.colors.sequential.Blues[2:]
    )

    # Create line chart for average amounts
    fig2 = px.line(
        amounts_df,
        x='Year',
        y='Average Amount',
        color='Category',
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Plotly
    )

    # Combine the figures
    for trace in fig2.data:
        trace.yaxis = "y2"
        fig1.add_trace(trace)

    # Update layout
    fig1.update_layout(
        height=600,
        hovermode='x unified',
        yaxis2=dict(
            title='Average Loan Amount ($)',
            overlaying='y',
            side='right',
            tickformat='$,.0f'
        ),
        yaxis=dict(title='Number of Students'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            tickformat='d'  # Force integer ticks for years
        )
    )

    return fig1

def plot_student_loan_percentages(df, selected_institution):
    # Filter data for selected institution
    df_filtered = df[df['institution name'] == selected_institution]
    
    # Define loan percentage metrics
    loan_metrics = {
        'All Student Loans'    : 'Percent of full-time first-time undergraduates awarded student loans',
        'Federal Student Loans': 'Percent of full-time first-time undergraduates awarded federal student loans',
        'Other Student Loans'  : 'Percent of full-time first-time undergraduates awarded other student loans'
    }
    
    # Create long format dataframe for plotting
    loan_data = []
    for metric, column in loan_metrics.items():
        data = df_filtered[['year', column]].copy()
        data['Loan Type'] = metric
        data['Percentage'] = data[column]
        loan_data.append(data[['year', 'Loan Type', 'Percentage']])
    
    loan_df = pd.concat(loan_data)
    
    # Create line plot
    fig = px.line(
        loan_df,
        x='year',
        y='Percentage',
        color='Loan Type',
        title='Share of Students Receiving Loans by Type',
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    # Update layout
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Percentage of Students",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(tickformat='d'),  # Force integer ticks for years
        yaxis=dict(tickformat='.1f')
    )
    
    # Add percentage labels
    fig.update_traces(
        texttemplate='%{y:.1f}%',
        textposition='top center'
    )

    return fig
