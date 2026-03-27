# Data Engineering & Clustering Implementation

This document explains the data engineering, feature creation, and clustering methods used in the project.

## Motivation
High-quality data and engineered features are essential for effective team optimization and role discovery.

## Key Components
- **Raw Data Processing**: Cleans and standardizes Pokémon stats, moves, and types.
- **Feature Engineering**: Adds advanced features such as type coverage, synergy scores, and move diversity.
- **Clustering**: Groups Pokémon by roles (e.g., sweeper, tank, support) using unsupervised learning (e.g., k-means, hierarchical clustering).

## Technical Details
- Uses pandas and NumPy for data manipulation.
- Clustering algorithms implemented with scikit-learn.
- Feature engineering is modular for easy experimentation.

## Results
Engineered features and clustering improve GA performance and enable more nuanced team composition.

For code, see `workflow/data/` and `workflow/src/utils/`.
