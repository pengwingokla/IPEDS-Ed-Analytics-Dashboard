import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 🔹 Load data with caching
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# 🔹 Net price by income
def plot_net_price_by_income(df, university_name):
    price_columns = [
        'average_net_price_income_0_30_000_students_awarded_title_iv_federal_financial_aid_2020_21',
        'average_net_price_income_30_001_48_000_students_awarded_title_iv_federal_financial_aid_2020_21',
        'average_net_price_income_48_001_75_000_students_awarded_title_iv_federal_financial_aid_2020_21',
        'average_net_price_income_75_001_110_000_students_awarded_title_iv_federal_financial_aid_2020_21',
        'average_net_price_income_over_110_000_students_awarded_title_iv_federal_financial_aid_2020_21'
    ]

    bracket_labels = ['$0–30k', '$30k–48k', '$48k–75k', '$75k–110k', '$110k+']

    # Filter by university name
    row = df[df['university_name'].str.lower() == university_name.lower()]
    if row.empty:
        return f"No data found for university: {university_name}"

    # Clean and convert to float
    prices = row[price_columns].iloc[0].replace(['PrivacySuppressed', 'NULL'], pd.NA).astype(float)

    # Plot
    fig = go.Figure(data=go.Bar(x=bracket_labels, y=prices, marker_color='orange'))
    fig.update_layout(
        title=f'{university_name}: Average Net Price by Income Bracket (2020–21)',
        xaxis_title='Family Income Bracket',
        yaxis_title='Average Net Price ($)',
        yaxis=dict(tickprefix="$"),
        template='plotly_white'
    )
    return fig

def plot_top20_institutions_by_total_aid(df):
    """
    Plot a stacked bar chart of total aid (grants, Pell, loans) for the top 20 institutions in NJ.
    Assumes columns: total_grants, total_pell, total_loans, unit_id.
    Requires get_school_name(unitid) to resolve school names.
    """
    # Sort and select top 20
    df_top = df.sort_values(by='total_amount_of_federal_state_local_institutional_or_other_sources_of_grant_aid_awarded_to_undergraduate_students', ascending=False).head(20).copy()

    # Create figure
    fig = go.Figure(data=[
        go.Bar(name='Total Grants', x=df_top['university_name'], y=df_top['total_amount_of_federal_state_local_institutional_or_other_sources_of_grant_aid_awarded_to_undergraduate_students']),
        go.Bar(name='Total Pell Grants', x=df_top['university_name'], y=df_top['total_amount_of_federal_student_loans_awarded_to_undergraduate_students']),
        go.Bar(name='Total Loans', x=df_top['university_name'], y=df_top['total_amount_of_pell_grant_aid_awarded_to_full_time_first_time_undergraduates'])
    ])

    # Customize layout
    fig.update_layout(
        barmode='stack',
        title="Top 20 NJ Institutions by Total Aid Disbursed (Grants + Pell + Loans)",
        xaxis_title="Institution Name",
        yaxis_title="Total Aid Amount (USD)",
        xaxis_tickangle=45,
        template="plotly_white"
    )

    return fig

def plot_aid_type_breakdown_percent(df, university_name):
    """
    Create a 100% stacked bar chart showing the percentage breakdown of total aid
    (grants, Pell grants, loans) per institution.
    """
    # Column definitions
    grant_col = 'total_amount_of_federal_state_local_institutional_or_other_sources_of_grant_aid_awarded_to_undergraduate_students'
    pell_col = 'total_amount_of_federal_pell_grant_aid_awarded_to_undergraduate_students'
    loan_col = 'total_amount_of_federal_student_loans_awarded_to_undergraduate_students'

    # Filter the row for the specified school
    row = df[df['university_name'].str.lower() == university_name.lower()]
    if row.empty:
        return f"No data found for '{university_name}'"

    # Extract and fill NA
    grant = row[grant_col].values[0] or 0
    pell = row[pell_col].values[0] or 0
    loan = row[loan_col].values[0] or 0
    total = grant + pell + loan

    if total == 0:
        return f"Aid data is missing or zero for '{university_name}'"

    # Calculate percentages
    data = {
        'Other Grants': grant / total * 100,
        'Pell Grants': pell / total * 100,
        'Loans': loan / total * 100
    }

    # Plot horizontal bar chart
    fig = go.Figure(go.Bar(
        x=list(data.values()),
        y=list(data.keys()),
        orientation='h',
        marker_color=['cornflowerblue', 'salmon', 'lightgreen']
    ))

    fig.update_layout(
        title=f"{university_name}: Aid Type Breakdown (% of Total Aid)",
        xaxis_title="% of Total Aid",
        yaxis_title="Aid Type",
        xaxis=dict(range=[0, 100]),
        template='plotly_white'
    )

    return fig