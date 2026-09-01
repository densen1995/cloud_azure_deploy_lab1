"""File-path and backend constants."""

import os
from pathlib import Path

# Folders that hold the images and the markdown text used by the pages.
ASSETS_PATH = Path(__file__).parents[1] / "assets"
IMAGE_PATH = ASSETS_PATH / "image"
MARKDOWN_PATH = ASSETS_PATH / "markdown"

# Where the backend API lives.
# - Locally it defaults to http://127.0.0.1:8000.
# - In Docker Compose it is set to http://backend:8000 (the service name).
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")