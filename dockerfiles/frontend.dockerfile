# Frontend image: Streamlit multipage app.
FROM python:3.13-slim

WORKDIR /app

# Copy the frontend package (code + assets) into the image.
COPY frontend/ /app/

# Installs uv, then install the frontend dependencies from pyproject.toml.
RUN pip install --no-cache-dir uv
RUN uv sync --no-dev

# Run streamlit from the folder where app.py lives so it finds the pages/ folder.
WORKDIR /app/src/frontend

CMD ["uv", "run", "streamlit", "run", "app.py", \
     "--server.address", "0.0.0.0", "--server.port", "8501"]