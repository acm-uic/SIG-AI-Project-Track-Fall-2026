
# Genetic Algorithm (GA) Implementation: Technical Report

This document provides a comprehensive, data-driven explanation of the genetic algorithm (GA) engine for Pokémon team optimization, including motivation, architecture, ablation studies, and key results.

---

## Motivation
The GA is designed to efficiently search the enormous combinatorial space of Pokémon teams, optimizing for competitive viability, diversity, and legality. It enables:
- Discovery of high-performing teams for competitive formats
- Analysis of how different algorithmic choices affect team quality and diversity
- Reproducible, data-driven research for both academic and practical applications

---

## GA Architecture & Configurations

### Core Components
| Component         | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Initialization    | Teams generated via uniform, inverse, or sqrt-weighted sampling             |
| Fitness Function  | Weighted sum of base stats, type coverage, synergy, diversity, penalties    |
| Selection         | Tournament selection (k=3), favoring high-fitness teams                     |
| Crossover         | Mixes parent teams to create offspring, promoting strategy recombination     |
| Mutation          | Randomly swaps Pokémon or moves to maintain exploration                     |
| Elitism           | Top 5 teams preserved each generation to ensure progress                    |

### Example Configurations

#### Baseline (ConfigA)
```yaml
population:
	size: 150
	generations: 250
	tournament_k: 3
	elitism: 5
fitness:
	base_stats_weight: 0.4
	type_coverage_weight: 0.3
	synergy_weight: 0.15
	diversity_weight: 0.0
	imbalance_lambda: 0.0
	weakness_lambda: 0.0
initialization:
	method: uniform
```

#### Inverse Weighted (ConfigB)
```yaml
population:
	size: 150
	generations: 250
	tournament_k: 3
	elitism: 5
fitness:
	base_stats_weight: 0.4
	type_coverage_weight: 0.3
	synergy_weight: 0.15
	diversity_weight: 0.0
	imbalance_lambda: 0.0
	weakness_lambda: 0.1
initialization:
	method: inverse
```

#### Full (ConfigC)
```yaml
population:
	size: 150
	generations: 250
	tournament_k: 3
	elitism: 5
fitness:
	base_stats_weight: 0.4
	type_coverage_weight: 0.3
	synergy_weight: 0.15
	diversity_weight: 0.15
	imbalance_lambda: 0.2
	weakness_lambda: 0.1
initialization:
	method: sqrt_weighted
```

---

## Ablation Study: Summary Table

| Config         | Init      | Diversity | Imbalance | Weakness | Final Mean Fitness | Final Max Fitness | Final Std | Mean Entropy | Rare Archetype % | Best Team Fitness | Convergence Gen | Time (s) |
|---------------|-----------|-----------|-----------|----------|-------------------|-------------------|-----------|--------------|------------------|-------------------|-----------------|----------|
| ConfigA       | uniform   | 0.0       | 0.0       | 0.0      | 0.716             | 0.724             | 0.021     | 1.78         | 100.0            | 0.724             | 132             | 218.7    |
| ConfigB       | inverse   | 0.0       | 0.0       | 0.1      | 0.641             | 0.649             | 0.023     | 2.24         | 98.7             | 0.649             | 250             | 303.8    |
| ConfigC       | sqrt_wt   | 0.15      | 0.2       | 0.1      | 0.721             | 0.732             | 0.032     | 2.55         | 100.0            | 0.732             | 250             | 198.5    |

---

## Statistical Significance (t-tests)

| Config 1      | Config 2      | Mean Diff | t-statistic | p-value         | Cohen's d | Significant? |
|--------------|---------------|-----------|-------------|-----------------|-----------|--------------|
| A Baseline   | B InverseWt   | 0.078     | 158.17      | 1.82e-52        | 51.32     | Yes          |
| A Baseline   | C Full        | -0.003    | -4.14       | 2.86e-4         | -1.34     | Yes          |
| B InverseWt  | C Full        | -0.080    | -114.41     | 1.75e-44        | -37.12    | Yes          |

---

## Fitness Progression (Sample: ConfigA vs ConfigC)

| Gen | Mean Fitness (A) | Max Fitness (A) | Mean Fitness (C) | Max Fitness (C) |
|-----|------------------|-----------------|------------------|-----------------|
| 0   | 0.472            | 0.609           | 0.394            | 0.561           |
| 5   | 0.596            | 0.655           | 0.537            | 0.632           |
| 10  | 0.652            | 0.676           | 0.602            | 0.690           |
| 15  | 0.670            | 0.689           | 0.645            | 0.717           |
| 18  | 0.677            | 0.689           | 0.680            | 0.717           |
| Final | 0.716          | 0.724           | 0.721            | 0.732           |

---

## Best Teams (Final Generation)

### ConfigA (Baseline)
| Rank | Fitness | Team                                                      | Archetypes                                      |
|------|---------|-----------------------------------------------------------|-------------------------------------------------|
| 1    | 0.724   | koraidon, groudon, yveltal, miraidon, kyogre, dialga      | Generalist, Generalist, Generalist, Speed Sweeper, Balanced All-Rounder, Defensive Pivot |

### ConfigB (Inverse Weighted)
| Rank | Fitness | Team                                                      | Archetypes                                      |
|------|---------|-----------------------------------------------------------|-------------------------------------------------|
| 1    | 0.649   | eternatus, zekrom, volcanion, regigigas, zamazenta, lunala| Defensive Pivot, Speed Sweeper, Balanced All-Rounder, Generalist, Generalist, Fast Attacker |

### ConfigC (Full)
| Rank | Fitness | Team                                                      | Archetypes                                      |
|------|---------|-----------------------------------------------------------|-------------------------------------------------|
| 1    | 0.732   | baxcalibur, groudon, flutter-mane, stakataka, miraidon, mewtwo | Balanced All-Rounder, Generalist, Defensive Pivot, Defensive Wall, Speed Sweeper, Fast Attacker |

---

## Key Insights
- Adding diversity and penalty terms (ConfigC) improves both fitness and team variety.
- All configurations converge to high fitness, but ConfigC achieves the best balance of performance and diversity.
- Statistical tests confirm that differences between configurations are significant.

---

For code, see [`workflow/src/ga/`](../workflow/src/ga/). For full experiment logs and additional plots, see [`workflow/reports/ga_results/`](../workflow/reports/ga_results/).
