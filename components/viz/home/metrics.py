import streamlit as st
import pandas as pd

def grad_rate_metrics(df, selected_institution="New Jersey Institute of Technology"):
    # Filter data for the selected institution
    df_filtered = df[df['institution name'] == selected_institution].copy()

    if df_filtered.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Sort by year to ensure proper order
    df_filtered = df_filtered.sort_values('year')
    
    # Get graduation rate data over time
    grad_rates = df_filtered['Graduation rate, total cohort'].tolist()
    
    # Get the most recent graduation rate and calculate delta
    latest_grad_rate = grad_rates[-1]
    prev_grad_rate = grad_rates[-2] if len(grad_rates) > 1 else latest_grad_rate
    delta = latest_grad_rate - prev_grad_rate

    # Display metric with line chart
    st.metric(
        f"Graduation Rate {df_filtered['year'].iloc[-1]}",
        f"{latest_grad_rate:.1f}%",
        f"{delta:+.1f}%",
        # chart_data=grad_rates,
        # chart_type="line",
        # border=True,
        width="stretch",
        height="content"
    )
    
    return df_filtered

def admission_yield_metrics(df, selected_institution="New Jersey Institute of Technology"):
    # Filter data for the selected institution
    df_filtered = df[df['institution name'] == selected_institution].copy()

    if df_filtered.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Sort by year to ensure proper order
    df_filtered = df_filtered.sort_values('year')
    
    # Calculate yield rate using IPEDS yield metric
    df_filtered['yield_rate'] = df_filtered['Admissions yield - total']
    
    yield_rates = df_filtered['yield_rate'].tolist()
    
    # Get the most recent yield rate and calculate delta
    latest_yield = yield_rates[-1]
    prev_yield = yield_rates[-2] if len(yield_rates) > 1 else latest_yield
    delta = latest_yield - prev_yield

    # Display metric with line chart
    st.metric(
        f"Admission Yield {df_filtered['year'].iloc[-1]}", 
        f"{latest_yield:.1f}%",
        f"{delta:+.1f}%",
        # chart_data=yield_rates,
        # chart_type="bar",
        # border=True,
        width="stretch",
        height="content"
    )
    return df_filtered

def selectivity_metrics(df, selected_institution="New Jersey Institute of Technology"):
    # Filter data for the selected institution
    df_filtered = df[df['institution name'] == selected_institution].copy()

    if df_filtered.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Sort by year to ensure proper order
    df_filtered = df_filtered.sort_values('year')
    
    # Calculate selectivity using IPEDS percent admitted metric
    df_filtered['selectivity_rate'] = df_filtered['Percent admitted - total']
    
    selectivity_rates = df_filtered['selectivity_rate'].tolist()
    
    # Get the most recent selectivity rate and calculate delta
    latest_selectivity = selectivity_rates[-1]
    prev_selectivity = selectivity_rates[-2] if len(selectivity_rates) > 1 else latest_selectivity
    delta = latest_selectivity - prev_selectivity

    # Display metric with line chart
    st.metric(
        f"Selectivity Rate {df_filtered['year'].iloc[-1]}", 
        f"{latest_selectivity:.1f}%",
        f"{delta:+.1f}%",
        width="stretch",
        height="content"
    )
    return df_filtered


def aid_metrics(df, selected_institution="New Jersey Institute of Technology"):
    # Filter data for the selected institution
    df_filtered = df[df['institution name'] == selected_institution].copy()

    if df_filtered.empty:
        raise ValueError(f"No data found for institution: {selected_institution}")

    # Sort by year to ensure proper order
    df_filtered = df_filtered.sort_values('year')
    
    # Get the aid percentage column
    aid_col = 'Percent of full-time first-time undergraduates awarded any loans to students or grant aid  from federal state/local government or the institution'
    aid_rates = df_filtered[aid_col].tolist()
    
    # Get the most recent aid rate and calculate delta
    latest_aid = aid_rates[-1]
    prev_aid = aid_rates[-2] if len(aid_rates) > 1 else latest_aid
    delta = latest_aid - prev_aid

    # Display metric with line chart
    st.metric(
        f"Students Receiving Aid {df_filtered['year'].iloc[-1]}", 
        f"{latest_aid:.1f}%",
        f"{delta:+.1f}%",
        width="stretch",
        height="content"
    )
    return df_filtered
