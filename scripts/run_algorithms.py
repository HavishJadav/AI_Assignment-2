import os
import sys
import time
import multiprocessing
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.branch_and_bound import branch_and_bound
from algorithms.ida_star import ida_star
from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from environments.frozen_lake_env import frozen_lake_env
from environments.ant_maze_env import ant_maze_env
from environments.tsp_env import generate_tsp_env

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
    successful_runs = 0
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
            successful_runs += 1
            results.append(f"Run {i + 1}: Cost={cost}, Time={run_time:.4f} sec, Path={path}")
    avg_time = total_time / successful_runs if successful_runs > 0 else float('inf')
    results.append(f"\nAverage Time over {successful_runs} runs: {avg_time:.4f} sec")
    return "\n".join(results), avg_time

def run_frozen_lake():
    print("Running Branch and Bound on Frozen Lake")
    result, avg_time = run_multiple("Branch and Bound (Frozen Lake)", branch_and_bound, args=("FrozenLake-v1",))
    print(result)
    write_result("bnb.txt", result)
    return "Branch and Bound", avg_time

def run_ant_maze():
    print("Running IDA* on Ant Maze")
    result, avg_time = run_multiple("IDA* (Ant Maze)", ida_star, env=ant_maze_env)
    print(result)
    write_result("ida_star.txt", result)
    return "IDA*", avg_time

def run_tsp():
    print("Running TSP with Hill Climbing and Simulated Annealing")
    matrix = generate_tsp_env(5)

    result_hc, avg_time_hc = run_multiple("Hill Climbing (TSP)", hill_climbing, args=(matrix,))
    print(result_hc)
    write_result("hill_climbing.txt", result_hc)

    result_sa, avg_time_sa = run_multiple("Simulated Annealing (TSP)", simulated_annealing, args=(matrix,))
    print(result_sa)
    write_result("simulated_annealing.txt", result_sa)

    return [("Hill Climbing", avg_time_hc), ("Simulated Annealing", avg_time_sa)]

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)

    algo_times = []

    bnb_label, bnb_time = run_frozen_lake()
    algo_times.append((bnb_label, bnb_time))

    ida_label, ida_time = run_ant_maze()
    algo_times.append((ida_label, ida_time))

    tsp_results = run_tsp()
    algo_times.extend(tsp_results)

    # Plotting
    labels, times = zip(*algo_times)
    plt.figure(figsize=(10, 6))
    plt.bar(labels, times, color='skyblue')
    plt.xlabel("Algorithm")
    plt.ylabel("Average Time (s)")
    plt.title("Average Execution Time of Algorithms")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTS_DIR, "average_times.png"))
    print("Saved average_times.png in results directory.")
