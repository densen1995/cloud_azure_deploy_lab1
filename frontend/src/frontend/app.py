"""Entrypoint that runs the eClipseBord app."""

import streamlit as st

st.set_page_config(
    page_title="eClipseBord",
    page_icon="🌘",
    layout="wide",
)

# The pages that show up in the sidebar. Paths are relative to this file.
pages = [
    st.Page("pages/home.py", title="Home", icon="🌘"),
    st.Page("pages/charts.py", title="Charts", icon="📊"),
    st.Page("pages/data.py", title="Data", icon="📄"),
]

pg = st.navigation(pages)  # builds the sidebar navigation menu
pg.run()                   # runs the page the user selected
