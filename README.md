# eClipseBord

A small **fullstack solar eclipse dashboard**, built with **FastAPI + Streamlit**,
containerized with **Docker**, and ready to deploy to **Azure**.

The data is NASA's five-millennium catalog of solar eclipses.

## Project structure

```
cloud_azure_deploy_lab/            
├── pyproject.toml                 # workspace (members: backend, frontend)
├── docker-compose.yaml            # runs both services together                      
│
├── data/                          # shared dataset (used by EDA + backend)
│   └── solar.csv
│
├── notebooks/                           # short exploratory data analysis 
│   └── eda.ipynb
│
├── dockerfiles/
│   ├── backend.dockerfile
│   └── frontend.dockerfile
│
├── backend/                       # FastAPI service
│   └── src/backend/
│       ├── api.py                 # the GET endpoints
│       ├── data_processing.py     # loads + cleans the dataset
│       └── constants.py           # where the data lives
│       └── pyproject.toml
└── frontend/                      # Streamlit multipage app
    └── src/frontend/
        ├── app.py                 # entrypoint (st.navigation + st.Page)
        ├── pages/                 # home, charts, data
        ├── components/            # kpis.py, charts.py
        ├── utils/                 # constants.py, helpers.py
        └── assets/                # image/ (eclipse.png) + markdown/
        └── pyproject.toml
``` 
## Run locally (without Docker)

```bash
# 1. setup uv workspaces/ frontend and backend packages 
uv sync installs all packages (and uv init /creates .venv/pyproject.toml)


# 2. start the backend (terminal 1)
uv run uvicorn api:app --reload --app-dir backend/src/backend

# 3. start the frontend (terminal 2)
uv run streamlit run frontend/src/frontend/app.py
```

- Backend docs: http://127.0.0.1:8000/docs
- Frontend:     http://localhost:8501

## Run locally with Docker

```bash
docker compose up --build
```

Same URLs as above. The frontend reaches the backend through the compose
network (`BACKEND_URL=http://backend:8000`).

## Deploy to Azure
Step by step guide on deployment available in azure provider documentation online.

## Backend endpoints

| Method | Path                        | Description                              |
| ------ | --------------------------- | ---------------------------------------- |
| GET    | `/`                         | Welcome message                          |
| GET    | `/eclipses?limit=100`       | First N eclipse records                  |
| GET    | `/eclipses/stats`           | Totals + year range + average magnitude  |
| GET    | `/eclipses/types`           | Count per eclipse type                   |
| GET    | `/eclipses/by-period`       | Count per 100-year period                |
| GET    | `/eclipses/locations`       | Lat/lon points for the map               |
| GET    | `/eclipses/type/{type}`     | Filter by type (e.g. `Total`)            |


Developer: Dennis C
