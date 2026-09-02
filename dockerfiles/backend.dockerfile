# Backend image: FastAPI served by uvicorn.
FROM python:3.13-slim

WORKDIR /app

# Copy the backend package and the shared dataset into the image.
COPY backend/ /app/
COPY data/ /app/data/

# Installs uv, then install the backend dependencies from pyproject.toml.
RUN pip install --no-cache-dir uv
RUN uv sync --no-dev

# Tell the app where the dataset is located
ENV DATA_DIR=/app/data

# Run the API from the folder where api.py lives.
WORKDIR /app/src/backend

CMD ["uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]