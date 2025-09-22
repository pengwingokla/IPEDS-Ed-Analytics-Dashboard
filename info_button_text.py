"""
Info Button Text Module

This module contains all the help text for the info buttons (𝒾) used throughout the application.
The text is organized by category for easy maintenance and reuse.
"""

# =============================================================================
# ENROLLMENT SECTION HELP TEXT
# =============================================================================

def get_enrollment_donut_chart_help():
    """Help text for the enrollment donut chart showing NJIT vs other NJ schools."""
    return "This donut chart visualizes the proportion of **total undergraduate enrollment** of the selected institution compared to the rest of New Jersey's higher education institutions. It provides a quick snapshot of how the selected school contributes to the overall state enrollment for the chosen year."

def get_enrollment_trends_help():
    """Help text for the enrollment trends bar chart showing NJIT's share change over time."""
    return "This bar chart illustrates undergraduate enrollment trends over time, comparing the selected institution's enrollment to that of all other NJ schools. It also shows the annual change in the selected institution's share of total enrollment compared to the year before it to evaluate relative growth or decline over multiple years."

def get_full_vs_part_time_trend_help():
    """Help text for the full-time vs part-time enrollment trend chart."""
    return "This line chart visualizes the yearly trend of first-time, degree/certificate-seeking students enrollment categorized by full-time and part-time status to help identifying shifts in institutional attendance patterns."

def get_admission_funnel_help():
    """Help text for the admission funnel chart."""
    return "This funnel chart illustrates the admissions pipeline for a selected institution and year. It breaks down the total number of applicants, how many were admitted, and how many ultimately enrolled, providing a clear view of conversion at each stage of the enrollment process."

def get_total_enrollment_help():
    """Help text for the total enrollment bar chart."""
    return "Total undergraduate enrollment by institution."

def get_gender_enrollment_help():
    """Help text for the gender enrollment chart."""
    return "Enrollment by gender for selected institutions."

def get_admission_yield_rate_help():
    """Help text for the admission rate and yield rate chart."""
    return "This grouped bar chart compares the admission rate and yield rate across selected institutions for a specific year. Admission rate represents the percentage of applicants who were admitted, while yield rate indicates the percentage of admitted students who chose to enroll. This visualization helps assess the selectivity and enrollment effectiveness of different institutions."

# =============================================================================
# GRADUATION SECTION HELP TEXT
# =============================================================================

def get_graduation_funnel_help():
    """Help text for the graduation funnel chart."""
    return """
    The graduation funnel tracks an entering cohort across years, showing outcomes such as on-time and extended graduates, students still enrolled, transfer-outs, and non-completers. The selected year displays cumulative results up to that point, offering a clear snapshot of the cohort’s educational progress, persistence, and final outcomes over time. 
    Example when selected_year = 2023. The graduation funnel shows the 2017 cohort’s outcomes as of 2023: 4-, 5-, and 6-year graduates, students still enrolled, transfer-outs, and non-completers. These categories add up to nearly 100% of the original cohort, revealing a complete picture of where students ended up after six years.
    """

# =============================================================================
# FINANCIAL AID SECTION HELP TEXT
# =============================================================================

def get_top20_institutions_aid_help():
    """Help text for the top 20 institutions by total aid chart."""
    return "This chart displays the top 20 institutions by total aid disbursed (grants + Pell + loans) in New Jersey. It helps identify the institutions that provide the highest financial assistance to students."

def get_net_price_by_income_help():
    """Help text for the net price by income chart."""
    return "This chart shows the average net price paid by students in different family income brackets after accounting for all forms of financial aid. Net price represents the actual out-of-pocket cost for students and families."

def get_aid_type_breakdown_help():
    """Help text for the aid type breakdown chart."""
    return "This chart shows the percentage breakdown of total aid (grants, Pell, loans) per institution."
