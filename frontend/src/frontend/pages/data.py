import streamlit as st
from frontend.utils.helpers import get_dataframe


def data():
    st.markdown("# 📄 Data")

    #the user chooses how many rows to pull from the API.
    limit = st.slider("Number of rows to load", min_value=10, max_value=1000, value=100, step=10)

    df = get_dataframe(f"/eclipses?limit={limit}")
    st.write(f"Showing {len(df)} rows")
    st.dataframe(df, width="stretch")


if __name__ == "__main__":
    data()
