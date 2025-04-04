import time
import os
from algorithms.branch_and_bound import branch_and_bound
from algorithms.ida_star import ida_star
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from environments.frozen_lake_env import frozen_lake_env
from environments.ant_maze_env import ant_maze_env
from environments.tsp_env import generate_tsp_env

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def write_result(file_name, content):
    with open(os.path.join(RESULTS_DIR, file_name), 'w') as f:
        f.write(content)

def run_frozen_lake():
    env = frozen_lake_env()
    start_time = time.time()
    path, cost = branch_and_bound()
    end_time = time.time()
    result = f"BnB Solution: {path}\nCost: {cost}\nTime Taken: {end_time - start_time:.4f} sec\n"
    print(result)
    write_result("bnb.txt", result)

def run_ant_maze():
    env = ant_maze_env()
    start_time = time.time()
    path, cost = ida_star()
    end_time = time.time()
    result = f"IDA* Solution: {path}\nCost: {cost}\nTime Taken: {end_time - start_time:.4f} sec\n"
    print(result)
    write_result("ida_star.txt", result)

def run_tsp():
    distance_matrix = generate_tsp_env(5)

    start_time = time.time()
    hc_path, hc_cost = hill_climbing(distance_matrix)
    end_time = time.time()
    hc_result = f"Hill Climbing Solution: {hc_path}\nCost: {hc_cost}\nTime Taken: {end_time - start_time:.4f} sec\n"
    print(hc_result)
    write_result("hill_climbing.txt", hc_result)

    start_time = time.time()
    sa_path, sa_cost = simulated_annealing(distance_matrix)
    end_time = time.time()
    sa_result = f"Simulated Annealing Solution: {sa_path}\nCost: {sa_cost}\nTime Taken: {end_time - start_time:.4f} sec\n"
    print(sa_result)
    write_result("simulated_annealing.txt", sa_result)

if __name__ == "__main__":
    print("Running Frozen Lake (Branch and Bound)")
    run_frozen_lake()
    print("\nRunning Ant Maze (IDA*)")
    run_ant_maze()
    print("\nRunning Traveling Salesman Problem (Hill Climbing & Simulated Annealing)")
    run_tsp()
