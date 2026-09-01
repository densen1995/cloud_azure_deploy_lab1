import streamlit as st

from frontend.components.charts import type_bar_chart, period_line_chart, location_map


def charts():
    st.markdown("# 📊 Charts")

    st.subheader("Eclipses per type")
    type_bar_chart()

    st.subheader("Eclipses per 100-year period")
    period_line_chart()

    st.subheader("Where eclipses happen")
    st.caption("Each dot is where an eclipse reached its maximum.")
    location_map()


if __name__ == "__main__":
    charts()