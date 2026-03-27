# App Directory

This directory contains the user-facing frontend and backend for the Pokémon Team Optimization project.

## Contents
- **streamlit_app.py**: Streamlit UI for interactive team generation, analysis, and visualization.
- **api.py**: FastAPI backend serving GA results, data, and business logic via REST endpoints.
- **utils.py**: Shared utility functions for both frontend and backend.

## How to Use
- Run the backend (api.py) to serve data and GA results.
- Launch the frontend (streamlit_app.py) for the interactive user interface.
- Use utils.py for common logic shared between frontend and backend.

The app is modular, with a clear separation between UI and business logic for maintainability and scalability.

## Overview
- **streamlit_app.py**: The interactive Streamlit web frontend. Lets users generate, analyze, and download competitive Pokémon teams, and explore detailed stats, archetypes, and role assignments.
- **api.py**: FastAPI backend that exposes endpoints for running the genetic algorithm, serving Pokémon data, and supporting the frontend. All business logic is handled in the backend for modularity and scalability.
- **utils.py**: Shared utility functions for data normalization, stat extraction, and composition presets, used by both frontend and backend.

## Key Features
- **Separation of Concerns**: The frontend is a pure UI layer, while the backend handles all computation and data logic. This enables robust testing, scalability, and future deployment flexibility.
- **API-First Architecture**: All team generation, analysis, and data queries are performed via HTTP API calls, making the system extensible and easy to integrate with other tools.
- **Modern Python Stack**: Uses Streamlit for rapid UI prototyping and FastAPI for high-performance, production-ready APIs.

## How It Works
1. The user interacts with the Streamlit app to select modes (team generation, analysis, info, etc.).
2. The frontend sends requests to the FastAPI backend (e.g., `/run_ga`, `/data`).
3. The backend runs the genetic algorithm or serves data, returning results as JSON.
4. The frontend displays results, visualizations, and allows downloads.

## Why This Matters
- Demonstrates best practices in full-stack Python development.
- Enables reproducible, testable, and scalable AI workflows.
- Serves as a template for future research or production AI web apps.

For more technical details, see the main project README and the reports in `workflow/reports`.
