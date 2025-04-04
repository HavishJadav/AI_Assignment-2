import random
import numpy as np

def hill_climbing(distance_matrix):
    num_cities = len(distance_matrix)
    current_solution = list(range(num_cities))
    random.shuffle(current_solution)
    
    def total_distance(route):
        return sum(distance_matrix[route[i]][route[i+1]] for i in range(num_cities - 1)) + distance_matrix[route[-1]][route[0]]
    
    best_solution = current_solution[:]
    best_cost = total_distance(best_solution)
    
    for _ in range(1000):
        i, j = sorted(random.sample(range(num_cities), 2))
        new_solution = best_solution[:]
        new_solution[i:j+1] = reversed(new_solution[i:j+1])
        new_cost = total_distance(new_solution)
        
        if new_cost < best_cost:
            best_solution, best_cost = new_solution, new_cost
    
    return best_solution, best_cost