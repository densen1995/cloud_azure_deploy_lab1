"""Reusable helper functions (reading files and calling the backend)."""

from pathlib import Path

import httpx
import pandas as pd
import streamlit as st

from frontend.utils.constants import BACKEND_URL


def read_textfile(path: Path) -> str:
    """Open a text/markdown file and return its full contents as a string."""
    with open(path, encoding="utf-8") as file:
        return file.read()


@st.cache_data  # cache the result so we don't re-call the API on every rerun
def get_json(path: str):
    """GET a path from the backend and return the parsed JSON.

    Example: get_json("/eclipses/stats")
    """
    response = httpx.get(f"{BACKEND_URL}{path}", timeout=30)
    response.raise_for_status()
    return response.json()


@st.cache_data
def get_dataframe(path: str) -> pd.DataFrame:
    """Same as get_json, but returns the records as a pandas DataFrame."""
    return pd.DataFrame(get_json(path))
