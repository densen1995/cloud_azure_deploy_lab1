import pandas as pd
import streamlit as st
from frontend.utils.helpers import get_json


def type_bar_chart():
    """Bar chart: how many eclipses there are of each type."""
    types = get_json("/eclipses/types")  
    data = pd.DataFrame({"type": list(types.keys()), "count": list(types.values())})
    st.bar_chart(data, x="type", y="count")


def period_line_chart():
    """Line chart: number of eclipses per 100-year period."""
    periods = get_json("/eclipses/by-period")  # e.g. ("period": -2000, "count": 42)
    data = pd.DataFrame(periods)
    st.line_chart(data, x="period", y="count")


def location_map():
    """Map: where each eclipse reaches its maximum."""
    locations = get_json("/eclipses/locations")
    data = pd.DataFrame(locations)
    st.map(data)  # st.map automatically uses the 'lat' and 'lon' columns