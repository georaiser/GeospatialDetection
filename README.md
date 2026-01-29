# Autonomous Wildfire Monitoring System

A full-stack autonomous system for detecting and monitoring wildfires using real-time satellite imagery (GOES-16/18, VIIRS).

## Project Structure

This monorepo is divided into three main components:

- **[Engine](./engine/README.md)**: The AI/ML core. Handles satellite data ingestion, preprocessing, and fire detection using PyTorch, CrewAI, and LangGraph agents.
- **[Backend](./backend/README.md)**: FastAPI service for exposing detection data, managing the PostGIS database, and handling alerts.
- **[Frontend](./frontend/README.md)**: React (TypeScript) web application for visualizing active fires on an interactive 3D map.

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker (optional, for database)

### Quick Start

1.  **Initialize Engine:**

    ```bash
    cd engine
    pip install -r requirements.txt
    python main.py
    ```

2.  **Start Backend:**

    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn app.main:app --reload
    ```

3.  **Launch Frontend:**
    ```bash
    cd frontend
    npm install
    npm run dev
    ```

## Architecture

Data flows from the **Engine** (Ingestion -> Inference -> Agent Decision) to the **Backend** (PostGIS Persistance -> API) and finally to the **Frontend** (Visualization).

## Documentation

See [autonomous_wildfire_mvp.md](../autonomous_wildfire_mvp.md) for the detailed MVP specification.
