import pandas as pd 
from backend.constants import DATA_PATH

# The "Eclipse Type" column uses single-letter codes (sometimes with a suffix

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


