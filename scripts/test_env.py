import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from environments.frozen_lake_env import frozen_lake_env
from environments.ant_maze_env import ant_maze_env
from environments.tsp_env import generate_tsp_env

def test_frozen_lake():
    env = frozen_lake_env()
    print("Frozen Lake environment test successful.")

def test_ant_maze():
    env = ant_maze_env()
    print("Ant Maze environment test successful.")

def test_tsp():
    distance_matrix = generate_tsp_env(5)
    print("Generated TSP Distance Matrix:")
    print(distance_matrix)

def main():
    print("Testing Environments...")
    test_frozen_lake()
    test_ant_maze()
    test_tsp()
    print("All environment tests completed successfully.")

if __name__ == "__main__":
    main()