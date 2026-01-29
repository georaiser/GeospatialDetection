# Autonomous Wildfire Monitoring System - Full Stack MVP

## 1. Project Overview

This project is a modular, autonomous wildfire monitoring system designed to detect, verify, and alert on wildfire events using satellite imagery. It leverages a modern full-stack architecture separating the core AI/ML logic, the alerting/API backend, and the user-facing frontend.

**Core Technologies:**

- **Engine (AI/ML):** Python, PyTorch, LangGraph, CrewAI, Rasterio.
- **Backend (API):** FastAPI, PostgreSQL (PostGIS), SQLAlchemy/SQLModel.
- **Frontend (UI):** React (TypeScript), Vite, MapLibre/Cesium, TailwindCSS.

---

## 2. Directory Structure

The project is divided into three main monorepo-style directories:

```
wildfire/
├── engine/         # Python: AI Agents, Satellite Ingestion, ML Inference
├── backend/        # Python: FastAPI, Database management, User/Alert APIs
└── frontend/       # TypeScript: React web application for visualization
```

---

## 3. Component Details

### 3.1 Engine (`/engine`)

**Goal:** Autonomous processing of satellite data.
**Stack:** Python 3.10+, PyTorch, CrewAI/LangGraph.

**Agent Modules (`src/agents/`):**

- **Ingestion (`ingestion.py`):** Periodically fetches GOES-16/18 (5-10m) and VIIRS imagery.
- **Preprocessing (`preprocess_agent.py`):** Cloud masking, reprojection, thermal anomaly extraction.
- **Inference (`inference_agent.py`):**
  - _Detection:_ CNN/Transformer model to catch hotspots.
  - _Fusion:_ Merges GOES temporal resolution with VIIRS spatial resolution.
- **Decision/Fusion (`fusion.py`):** Uses LangGraph to validate event severity and reduce false positives.
- **Alerting (`alert_agent.py`):** Dispatches high-priority notifications.
- **Publisher (`map_publish_agent.py`):** Pushes confirmed detections to the **Backend** (PostGIS).

### 3.2 Backend (`/backend`)

**Goal:** Serve data to the frontend and manage alerts.
**Stack:** FastAPI, PostgreSQL (PostGIS), Pydantic.

**Responsibilities:**

- **API Layer:** REST endpoints for the frontend (`/detections`, `/alerts`, `/system-status`).
- **Database:** Stores geospatial data (Fire Polygons, Metadata).
- **Alerting System:** Handles email/SMS/Webhook dispatching based on Engine triggers.
- **Auth:** JWT Authentication for admin configurations.

### 3.3 Frontend (`/frontend`)

**Goal:** Visualization and Operational Command Dashboard.
**Stack:** React, TypeScript, Vite, TailwindCSS, Recharts.

**Features:**

- **Interactive Map:** 3D/2D view of active fires (Cesium or MapLibre).
- **Real-time Feed:** WebSocket/Polling connection to backend for incoming alerts.
- **Dashboard:** Graphs showing fire intensity over time, active satellite passes.
- **Admin Panel:** Configure detection thresholds and alert subscribers.

---

## 4. Data Flow Architecture

1.  **Ingestion (Engine):** Downloads Raw Satellite Data -> `data/raw`.
2.  **Processing (Engine):** ML Model extracts Hotspots -> `data/derived`.
3.  **Persist (Engine -> Backend):** Confirmed hotspots are written to PostGIS database.
4.  **Serve (Backend -> Frontend):** API serves GeoJSON to the React App.
5.  **Notify (Backend):** High-confidence events trigger Push Notifications.

---

## 5. Implementation Roadmap

### Phase 1: Foundation (Current Focus)

- **Engine:** Setup partial ingestion of GOES data and basic thresholding detector.
- **Backend:** Setup FastAPI + PostGIS + SQLAlchemy.
- **Frontend:** Scaffold React App with a basic Map component.

### Phase 2: Intelligence

- **Engine:** Integrate PyTorch detection model.
- **Engine:** Implement Agentic workflow (LangGraph) for false-positive reduction.
- **Frontend:** Add polished dashboard UI and realtime updates.

### Phase 3: Production & Scaling

- **Ops:** Docker Compose setup for all services.
- **Cloud:** Deploy to Cloud Run / AWS ECS.
- **Mobile:** Responsive adjustments for field usage.

---

## 6. License

MIT

---

## 7. Future Extensions

- **Drone Integration:** Autonomous dispatch for low-altitude verification of hotspots.
- **Weather Analysis:** Integration of wind vector models to predict fire spread direction.
- **LLM Reporting:** Automated generation of situation reports for emergency responders.
- **Multi-Hazard:** Expansion to detect volcanic activity, flooding, and smoke transport.
