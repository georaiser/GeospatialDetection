# Wildfire Engine

This directory contains the AI/ML core of the Autonomous Wildfire Monitoring System.

## Components

- **Ingestion Agent:** Downloads GOES & VIIRS Data.
- **Inference:** PyTorch models for hotspot detection.
- **Fusion/Decision:** LangGraph/CrewAI workflows for validation.

## Setup

```bash
pip install -r requirements.txt
python main.py
```
