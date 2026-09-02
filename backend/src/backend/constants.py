import os
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[3] / "data" #resolve makes the path absolute 

DATA_DIRECTORY = Path(os.getenv("DATA_DIR", DATA_PATH))