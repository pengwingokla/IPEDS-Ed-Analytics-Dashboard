import streamlit as st

def footer():
    """
    Simple footer with embedded URL
    """
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 10px; color: #666;">
        <a href="https://github.com/pengwingokla" target="_blank" 
           style="color: black; text-decoration: none;">
           Dashboard developed by <span style="color: #007bff;">Uyen Nguyen</span>
        </a>
        <br>
        <span style="font-size: 0.9em;">
            Built with Streamlit and Python
            <br> New Jersey Institute of Technology
        </span>
    </div>
    """, unsafe_allow_html=True)