# Traffic-Aware Intelligent Routing System

## Overview
This project explores traffic-aware route planning by combining graph search with traffic-related edge costs. The current version focuses on Boston's road network, a baseline A* implementation, and early-stage synthetic traffic generation for future model training.

## Motivation
Traditional navigation systems often rely on static shortest-path routing or simplified traffic assumptions. This project aims to build a routing system that can eventually account for time-varying traffic conditions and improve route recommendations.

## Current Progress
### Completed
- Configured the development environment
- Downloaded and explored Boston's road network using OSMnx
- Implemented a baseline A* search algorithm on the Boston road graph
- Planned a traffic feature pipeline with temporal, weather, and road-context features
- Reviewed literature on shortest path algorithms and traffic prediction

### In Progress
- Synthetic traffic data generation
- Feature engineering pipeline
- Preparing model-ready training data

### Next Steps
- Complete the traffic simulator
- Finalize engineered features
- Train an initial baseline prediction model
- Integrate predicted travel times into routing as dynamic edge weights

## Repository Structure
- src/data_collection/ : road network download and traffic simulation
- src/preprocessing/ : feature engineering
- src/routing/ : baseline A* and routing utilities
- notebooks/ : exploratory progress notebooks
- tests/ : basic validation tests
- docs/ : progress notes and literature notes

## Current Limitations
This repository does not yet include live traffic API integration, final ML models, or a deployed interface. It is intended to document the current development stage of the project.

## How to Run
Create a virtual environment, install requirements, and run the modules directly.

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/data_collection/osm_downloader.py
python src/routing/astar_baseline.py
