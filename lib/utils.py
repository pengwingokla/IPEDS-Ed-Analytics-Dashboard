import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_url(repo_id, filename, revision="main"):
    """ Normalize the URL for the HuggingFace dataset """
    return f"https://huggingface.co/datasets/{repo_id}/resolve/{revision}/{filename}"
