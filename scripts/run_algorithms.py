import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import multiprocessing
from algorithms.branch_and_bound import branch_and_bound
from algorithms.ida_star import ida_star
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from environments.frozen_lake_env import frozen_lake_env
from environments.ant_maze_env import ant_maze_env
from environments.tsp_env import generate_tsp_env

# Ensure root path is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

TIMEOUT = 600  # 10 minutes

def write_result(file_name, content):
    with open(os.path.join(RESULTS_DIR, file_name), 'w') as f:
        f.write(content)

def run_in_process(queue, func, *args):
    try:
        result = func(*args)
        queue.put(result)
    except Exception as e:
        queue.put(e)

def run_with_timeout(func, args=(), timeout=TIMEOUT):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_in_process, args=(queue, func, *args))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        return "TIMEOUT", None
    else:
        result = queue.get()
        if isinstance(result, Exception):
            return "ERROR", str(result)
        return result, None

def run_multiple(label, func, env=None, args=()):
    results = []
    total_time = 0.0
    for i in range(5):
        print(f"Run {i + 1} for {label}")
        if env:
            environment = env()
            args = (environment,) if args == () else args
        start_time = time.time()
        result, error = run_with_timeout(func, args=args)
        end_time = time.time()
        if result == "TIMEOUT":
            results.append(f"Run {i + 1}: TIMEOUT after {TIMEOUT} sec")
        elif result == "ERROR":
            results.append(f"Run {i + 1}: ERROR - {error}")
        else:
            path, cost = result
            run_time = end_time - start_time
            total_time += run_time
            results.append(f"Run {i + 1}: Cost={cost}, Time={run_time:.4f} sec, Path={path}")
    avg_time = total_time / 5
    results.append(f"\nAverage Time over 5 runs: {avg_time:.4f} sec")
    return "\n".join(results)

def run_frozen_lake():
    print("Running Branch and Bound on Frozen Lake")
    # result = run_multiple("Branch and Bound (Frozen Lake)", branch_and_bound, env=frozen_lake_env)
    result = run_multiple(
    "Branch and Bound (Frozen Lake)",
    branch_and_bound,
    args=("FrozenLake-v1",) )
    print(result)
    write_result("bnb.txt", result)


def run_ant_maze():
    print("Running IDA* on Ant Maze")
    result = run_multiple("IDA* (Ant Maze)", ida_star, env=ant_maze_env)
    print(result)
    write_result("ida_star.txt", result)

def run_tsp():
    print("Running TSP with Hill Climbing and Simulated Annealing")
    matrix = generate_tsp_env(5)

    result_hc = run_multiple("Hill Climbing (TSP)", hill_climbing, args=(matrix,))
    print(result_hc)
    write_result("hill_climbing.txt", result_hc)
    result_sa = run_multiple("Simulated Annealing (TSP)", simulated_annealing, args=(matrix,))
    print(result_sa)
    write_result("simulated_annealing.txt", result_sa)

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)  # Required for Windows
    run_frozen_lake()
    run_ant_maze()
    run_tsp()
    print("All algorithms have been run. Check the results in the 'results' directory.")