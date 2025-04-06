# AI Assignment 2 - Search Algorithms with Visualizations

This project implements and compares various search algorithms across different environments, measuring their performance and generating visualizations (GIFs) of their path-finding behavior.

---

## Features

- **Algorithms Implemented**:
  - Hill Climbing
  - Simulated Annealing
  - Branch and Bound (BnB)
  - Iterative Deepening A* (IDA*)

- **Environments Supported**:
  - Traveling Salesman Problem (TSP)
  - Frozen Lake (Grid World)
  - Ant Maze

- **Performance Analysis**:
  - Tracks execution time per run
  - Computes and plots average time to reach the goal state
  - Saves results to text files(results file) for reproducibility

- **Visualization**:
  - Also contain animated gifs for each algorithm in the results folder

---

## Installation

Ensure you have Python 3.10+ installed. Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Directory Structure

```
AI_Assignment-2/
├── algorithms/
│   ├── branch_and_bound.py
│   ├── hill_climbing.py
│   ├── ida_star.py
│   └── simulated_annealing.py
├── environments/
│   ├── tsp_env.py
│   ├── frozen_lake_env.py
│   └── ant_maze_env.py
├── results/
│   └── (Result logs, plots and GIFs are saved here)
├── scripts/
│   ├── create_gifs_new.py
│   └── create_gifs.py
│   └── run_algorithms.py
│   └── test_env.py
├── AI-Assignment 2.pptx
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Test if all environments are working correctly

```bash
python scripts/test_env.py
```
This will test if envs are running properly.

### 2. Run all algorithms and save results

```bash
python scripts/run_algorithms.py
```
This will run each algorithm 5 times and save the results,plot to the `results/` folder.

---

## Output Examples

### Results (Text Files)

- `results/bnb.txt`
- `results/ida_star.txt`
- `results/hill_climbing.txt`
- `results/simulated_annealing.txt`

Each file contains detailed results for 5 runs and the average time taken.

### Visuals

- `results/average_times.png` - Bar chart comparing all algorithms average times to reach the goal state
- `results/*.gif` - gif files for all algorithms
---

## Dependencies

```
gymnasium
numpy
matplotlib
imageio
```

## License
MIT License

---

## Authors
Manan Chavda(CS22B017)
Havish Jadav(CS22B026)

