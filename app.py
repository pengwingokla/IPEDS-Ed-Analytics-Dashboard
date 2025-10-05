import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu



from views.enrollment import show_enrollment_page
from views.graduation import show_graduation_page

# ---- Path Constants ----
IMG_NJIT_LOGO_PATH = "img/njit_logo.jpg"

# ---- Set Page Config ----
st.set_page_config(
    page_title="University Insights",
    page_icon=IMG_NJIT_LOGO_PATH,
    layout="wide"
)
# ---- Main Title ----
st.markdown("<h1 style='text-align: center;'>Higher Education Insights Dashboard</h1>", unsafe_allow_html=True)

# ---- Sidebar Navigation ----
# with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=["Home", "Enrollment", "Graduation", "Financial Aid"],
    icons=["house", "person-workspace", "mortarboard", "currency-dollar"], #https://icons.getbootstrap.com/
    default_index=0,
    orientation="horizontal")
if selected == "Home":
    st.session_state.active_page = "Welcome"
elif selected == "Enrollment":
    st.session_state.active_page = "Enrollment"
elif selected == "Graduation":
    st.session_state.active_page = "Graduation"
elif selected == "Financial Aid":
    st.session_state.active_page = "Financial Aid"

# ---- Default Welcome Page ----
if st.session_state.active_page == "Welcome":
    # st.markdown("# 👋")
    st.markdown("### Welcome to a Comprehensive View of NJIT's Performance")
    st.markdown("""
        This dashboard provides insights into institutional trends for NJIT and its 
        peer universities across New Jersey. Use the navigation menu on the left to explore:
        
        - **Statewide Enrollment Trends**
        - **Institution-Specific Enrollment & Admission**
        - **Multi-Institution Comparisons**
        
        Start by choosing a section from the sidebar.
    """)

# ---- Load datasets ----


# 🔸🔸 Enrollment Page 🔸🔸
if st.session_state.active_page == "Enrollment":
    show_enrollment_page()

# 🔸🔸 Graduation Page 🔸🔸
elif st.session_state.active_page == "Graduation":
    
    show_graduation_page()

# 🔸🔸 Financial Aid Page 🔸🔸
elif st.session_state.active_page == "Financial Aid":
    st.markdown("""### :orange[Financial Aid]""")
    sfa_data = load_data(SFA_PATH)

