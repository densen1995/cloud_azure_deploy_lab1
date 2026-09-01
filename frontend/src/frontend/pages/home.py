"""Home page - intro text and the key numbers."""

import streamlit as st

from frontend.utils.helpers import read_textfile
from frontend.utils.constants import IMAGE_PATH, MARKDOWN_PATH, BACKEND_URL
from frontend.components.kpis import show_kpis


def home():
    st.markdown("# 🌘 eClipseBord")
    st.image(IMAGE_PATH / "eclipse.png")
    st.markdown(read_textfile(MARKDOWN_PATH / "intro.md"))
    

    st.markdown("## Key numbers")
    try:
        show_kpis()
    except Exception:  # keep the page alive if the backend is unreachable
        st.warning(f"Could not reach the backend at {BACKEND_URL}. Is it running?")


if __name__ == "__main__":
    home()
