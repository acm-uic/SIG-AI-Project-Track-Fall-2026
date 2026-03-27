# Backend (FastAPI) Implementation

This document explains the design and technical details of the FastAPI backend for the Pokémon Team Optimization project.

## Motivation
The backend provides a robust, scalable API for running the genetic algorithm, serving data, and handling business logic.

## Key Components
- **API Endpoints**: `/run_ga`, `/data`, `/health` for optimization, data serving, and health checks.
- **Business Logic**: All optimization and data processing logic is handled server-side for security and reproducibility.
- **Serialization**: Robust handling of NaN/inf values for JSON compatibility.

## Technical Details
- Built with FastAPI for speed and async support.
- Modular code with shared utilities for maintainability.
- Designed for easy deployment to cloud or local servers.

For code, see `workflow/app/api.py` and `workflow/app/utils.py`.
