import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from lib.colors import NJIT_COLORS

from views.home import show_home_page
from views.enrollment.overview import show_enrollment_overview_page
from views.enrollment.statewide import show_enrollment_state_wide_trends_page
from views.enrollment.crossinst import show_enrollment_cross_institution_comparison_page
from views.graduation import show_graduation_page

# ---- Path Constants ----
IMG_NJIT_LOGO_PATH = "components/img/njit_logo.jpg"

# ---- Set Page Config ----
st.set_page_config(
    page_title="University Insights",
    page_icon=IMG_NJIT_LOGO_PATH, # Using an emoji instead of image path for tab icon
    layout="wide"
)
# ---- Main Title ----
st.markdown("<h1 style='text-align: center;'>Higher Education Insights Dashboard</h1>", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
selected = option_menu(
    menu_title=None,
    options=["Home", "Enrollment", "Graduation", "Financial Aid"],
    icons=["house", "person-workspace", "mortarboard", "currency-dollar"], #https://icons.getbootstrap.com/
    orientation="horizontal",
)

# 🔸🔸 Home Page 🔸🔸
if selected == "Home":
    st.session_state.active_page = "Home"
    show_home_page()

# 🔸🔸 Enrollment Page 🔸🔸
if selected == "Enrollment":
    selected_sub = option_menu(
        menu_title=None,
        options=["Overview", "State Wide Trends", "Cross-Institution Comparison"],
        icons=["building-fill", "globe-americas", "bar-chart-fill"],
        orientation="vertical",
    )
    if selected_sub == "Overview":
        show_enrollment_overview_page()
    elif selected_sub == "State Wide Trends":
        show_enrollment_state_wide_trends_page()
    elif selected_sub == "Cross-Institution Comparison":
        show_enrollment_cross_institution_comparison_page()
    # elif selected_sub == "Cross-Institution Comparison":
        


# 🔸🔸 Graduation Page 🔸🔸
elif selected == "Graduation":
    st.session_state.active_page = "Graduation"
    show_graduation_page()

# 🔸🔸 Financial Aid Page 🔸🔸
elif selected == "Financial Aid":
    st.session_state.active_page = "Financial Aid"