from fastapi import FastAPI
import pandas as pd

from backend.data_processing import df


"""FastAPI backend for eClipseBord.

Exposes some simple GET endpoints over the solar eclipse dataset.
Start it and open /docs to try them out interactively.
"""

app = FastAPI(title="eClipseBord API")

@app.get("/")
async def root():
    """Small welcome message so the root URL isn't empty."""
    return { "Welcome to the eClipseBord API"}


@app.get("/eclipses")
async def get_eclipses(limit: int = 100):
    """Return the first `limit` eclipse records as a list of dictionaries."""

    records = df.head(limit).to_dict(orient="records")

    for record in records:
        for key, value in record.items():
            if pd.isna(value):
                record[key] = None

    return records


@app.get("/eclipses/stats")
async def get_stats():
    """Return a few summary numbers about the whole dataset."""
    return {
        "total_eclipses": int(len(df)),
        "first_year": int(df["year"].min()),
        "last_year": int(df["year"].max()),
        "average_magnitude": round(float(df["Eclipse Magnitude"].mean()), 3),
    }

@app.get("/eclipses/types")
async def get_types():
    """Count how many eclipses there are of each main type."""
    counts = df["type_name"].value_counts()
    return counts.to_dict()


@app.get("/eclipses/locations")
async def get_locations(limit: int = 2000):
    """Return latitude/longitude points so the frontend can draw a map."""
    subset = df[["lat", "lon", "type_name", "Calendar Date"]].head(limit)
    return subset.to_dict(orient="records")

@app.get("/eclipses/type/{type_name}")
async def get_by_type(type_name: str):
    """Return eclipses of one type, e.g. /eclipses/type/Total (max 500 rows)."""
    filtered = df[df["type_name"].str.lower() == type_name.lower()]
    return filtered.head(500).to_dict(orient="records")


@app.get("/eclipses/by-period")
async def get_by_period():
    """Count eclipses grouped into 100-year periods ."""
    counts = df.groupby("period").size()
    return [{"period": int(period), "count": int(count)}
            for period, count in counts.items()]
