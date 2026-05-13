import numpy as np
import random

# Cities (x, y)
cities = np.array([
    [0, 0], [1, 5], [5, 2], [6, 6], [8, 3]
])
n = len(cities)

# Distance Matrix
dist = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist[i][j] = np.linalg.norm(cities[i] - cities[j])

# ACO Parameters
ants = 5
iterations = 10
alpha, beta = 1, 2
evaporation = 0.5
Q = 100
pheromone = np.ones((n, n))
best_path = None
best_length = float('inf')

# ACO Algorithm
for it in range(iterations):
    print(f"\n=== Iteration {it+1} ===")
    all_paths = []
    
    for ant in range(ants):
        path = [random.randint(0, n-1)]
        visited = set(path)
        
        while len(path) < n:
            current = path[-1]
            probs = []
            
            for j in range(n):
                if j not in visited:
                    tau = pheromone[current][j] ** alpha
                    eta = (1/dist[current][j]) ** beta
                    probs.append((j, tau * eta))
            
            next_city = random.choices(
                [p[0] for p in probs],
                weights=[p[1] for p in probs]
            )[0]
            
            path.append(next_city)
            visited.add(next_city)
            
        path.append(path[0]) # return
        
        length = sum(dist[path[i]][path[i+1]] for i in range(len(path)-1))
        all_paths.append((path, length))
        print(f"Ant {ant+1} Path: {path} Distance: {length:.2f}")
        
        if length < best_length:
            best_length = length
            best_path = path

    # Evaporation
    pheromone *= (1 - evaporation)
    
    # Update pheromone
    for path, length in all_paths:
        for i in range(len(path)-1):
            pheromone[path[i]][path[i+1]] += Q / length
            
    print(f"Best distance so far: {best_length:.2f}")

# Final Output
print("\n===== FINAL RESULT =====")
print("Best Path (City Index):", best_path)

# Show city coordinates
print("\nPath with Coordinates:")
for city in best_path:
    print(f"City {city} -> {cities[city]}")

print(f"\nShortest Distance Found: {best_length:.2f}")
