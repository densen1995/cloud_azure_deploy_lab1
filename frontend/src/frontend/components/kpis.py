import streamlit as st
from frontend.utils.helpers import get_json


def show_kpis():
    """Show three metric cards with the key numbers about the dataset."""
    stats = get_json("/eclipses/stats")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total eclipses", f"{stats['total_eclipses']:,}")
    col2.metric("Year range", f"{stats['first_year']} → {stats['last_year']}")
    col3.metric("Average magnitude", stats["average_magnitude"])