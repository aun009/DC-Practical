import numpy as np
import random

def aco_tsp(dist_matrix, n_ants=20, n_iterations=100, alpha=1, beta=2, evap=0.5, Q=100):
    n_cities = len(dist_matrix)
    pheromone = np.ones((n_cities, n_cities))
    best_path = None
    best_cost = float('inf')

    for it in range(n_iterations):
        all_paths = []
        all_costs = []
        for ant in range(n_ants):
            visited = [random.randint(0, n_cities-1)]
            while len(visited) < n_cities:
                current = visited[-1]
                unvisited = [i for i in range(n_cities) if i not in visited]
                probs = []
                for j in unvisited:
                    tau = pheromone[current][j] ** alpha
                    eta = (1.0 / (dist_matrix[current][j] + 1e-10)) ** beta
                    probs.append(tau * eta)
                probs = np.array(probs)
                probs /= probs.sum()
                next_city = np.random.choice(unvisited, p=probs)
                visited.append(next_city)
            cost = sum(dist_matrix[visited[i]][visited[i+1]] for i in range(n_cities-1))
            cost += dist_matrix[visited[-1]][visited[0]]
            all_paths.append(visited)
            all_costs.append(cost)
            if cost < best_cost:
                best_cost = cost
                best_path = visited.copy()

        # Update pheromones
        pheromone *= (1 - evap)
        for path, cost in zip(all_paths, all_costs):
            for i in range(n_cities-1):
                pheromone[path[i]][path[i+1]] += Q / cost
            pheromone[path[-1]][path[0]] += Q / cost

        print(f"Iter {it}: Best cost = {best_cost}")

    return best_path, best_cost

if __name__ == "__main__":
    # Example distance matrix for 5 cities
    dist = np.array([
        [0, 2, 9, 10, 7],
        [2, 0, 6, 4, 3],
        [9, 6, 0, 8, 5],
        [10, 4, 8, 0, 6],
        [7, 3, 5, 6, 0]
    ])
    path, cost = aco_tsp(dist)
    print("Best path:", path)
    print("Best cost:", cost)