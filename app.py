import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu



from pages.enrollment import show_enrollment_page

# ---- Path Constants ----
IMG_NJIT_LOGO_PATH = "img/njit_logo.jpg"
ADMS_PATH = "data/archives/NJ_admission_data.csv"
EFFY_PATH = "data/archives/NJ_enrollment_data.csv" 
SFA_PATH = "data/archives/NJ_sfa_data.csv"
GRAD_PATH = "data/archives/NJ_graduation_data.csv"
CUSTOM_PATH = "data/custom/processed/c20-23.csv"

# ---- Set Page Config ----
st.set_page_config(
    page_title="University Insights",
    page_icon=IMG_NJIT_LOGO_PATH,
    layout="wide"
)

# ---- Load Data with Caching ----
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_url(repo_id, filename, revision="main"):
    """
    Normalize the URL for the HuggingFace dataset
    """
    return f"https://huggingface.co/datasets/{repo_id}/resolve/{revision}/{filename}"

# Initialize session states
if "active_page" not in st.session_state:
    st.session_state.active_page = "Welcome"

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

# ---- Main Title ----
st.title("Institutional Analytics")

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
adms_data = load_data(ADMS_PATH)
sfa_data = load_data(SFA_PATH)
dbt_enroll = load_data(normalize_url("chloecodes/IPEDS_ENROLLMENT", "enrollment.csv"))

# 🔸🔸 Enrollment Page 🔸🔸
if st.session_state.active_page == "Enrollment":
    show_enrollment_page()

# 🔸🔸 Graduation Page 🔸🔸
elif st.session_state.active_page == "Graduation":
    st.markdown("""### :orange[Graduation]""")
    grad_data = load_data(GRAD_PATH)
    dbt_grad = load_data(normalize_url("chloecodes/IPEDS_GRADUATION", "graduation.csv"))
    custom_df = load_data(CUSTOM_PATH)
    
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

# 🔸🔸 Financial Aid Page 🔸🔸
elif st.session_state.active_page == "Financial Aid":
    st.markdown("""### :orange[Financial Aid]""")
    sfa_data = load_data(SFA_PATH)

