import numpy as np

def generate_tsp_env(num_cities=5):
    np.random.seed(42)
    distance_matrix = np.random.randint(10, 100, size=(num_cities, num_cities))
    np.fill_diagonal(distance_matrix, 0)
    return distance_matrix