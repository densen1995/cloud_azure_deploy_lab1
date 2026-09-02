import pandas as pd 
from backend.constants import DATA_DIRECTORY

# The "Eclipse Type" column uses single-letter codes (sometimes with a suffix)

TYPE_NAMES = {
    "P": "Partial",
    "A": "Annular",
    "T": "Total",
    "H": "Hybrid",
}


def _parse_year(calendar_date: str) -> int:
    """Return the year as an int.

    Dates look like "-1999 June 12" or "2001 June 21". The year is always the
    first word and can be negative (years Before Common Era).
    """
    first_word = str(calendar_date).split()[0]
    return int(first_word)


def _parse_coordinate(value: str) -> float:
    """Turn a coordinate like "6.0N" or "33.3W" into a signed decimal number.

    North and East are positive, South and West are negative.
    """
    value = str(value).strip()
    direction = value[-1]        # last character: N, S, E or W
    number = float(value[:-1])   # everything before it is the number
    if direction in ("S", "W"):
        number = -number
    return number


  

def load_data() -> pd.DataFrame:
    """Read the CSV and add helper columns used by the API/charts."""
    df = pd.read_csv(DATA_DIRECTORY / "solar.csv")

    # Main eclipse category from the first letter of the type code.
    df["type_code"] = df["Eclipse Type"].str[0]
    df["type_name"] = df["type_code"].map(TYPE_NAMES).fillna("Other")


    # Parsed numeric helpers.
    df["year"] = df["Calendar Date"].apply(_parse_year)
    df["period"] = (df["year"] // 100) * 100  # group years into 100-year buckets
    df["lat"] = df["Latitude"].apply(_parse_coordinate)
    df["lon"] = df["Longitude"].apply(_parse_coordinate)

    return df

df = load_data()


