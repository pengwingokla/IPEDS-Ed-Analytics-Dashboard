import requests
import io
from PIL import Image
import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_url(repo_id, filename, revision="main"):
    """ Normalize the URL for the HuggingFace dataset """
    return f"https://huggingface.co/datasets/{repo_id}/resolve/{revision}/{filename}"


SOURCE_URL = "https://s.yimg.com/ny/api/res/1.2/1BfuHy5JmlehIC6C.4QlFQ--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD03NTA-/https://media.zenfs.com/en/globenewswire.com/33b1a8aac5d786b53279d9cf3cd45c4e"

def load_header_image(SOURCE_URL):
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            resp = requests.get(SOURCE_URL, headers=headers, timeout=10)
            resp.raise_for_status()
            img = Image.open(io.BytesIO(resp.content))
            return img
        except Exception as e:
            st.error(f"Failed to load header image: {e}")
            return None