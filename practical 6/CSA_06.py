import random
import numpy as np
import matplotlib.pyplot as plt

# Fitness Function (maximize)
def fitness(x):
    return x**2

# Initialize Population
def initialize_population(size, lower, upper):
    return [random.uniform(lower, upper) for _ in range(size)]

# Clone and Mutate
def clone_and_mutate(selected, clone_factor, mutation_rate):
    clones = []
    for i, x in enumerate(selected):
        for _ in range(clone_factor):
            # Adaptive mutation (better solution smaller mutation)
            mutation_strength = mutation_rate / (i + 1)
            mutated = x + random.uniform(-mutation_strength, mutation_strength)
            clones.append(mutated)
    return clones

# Replace worst individuals
def replace(pop, size, lower, upper):
    pop = sorted(pop, key=fitness, reverse=True)
    return pop[:size] + [random.uniform(lower, upper) for _ in range(size // 2)]

# Clonal Selection Algorithm
def clonal_selection(pop_size=20, generations=20, lower=-10, upper=10):
    population = initialize_population(pop_size, lower, upper)
    best_history = []

    for gen in range(generations):
        # Selection
        population = sorted(population, key=fitness, reverse=True)
        selected = population[:pop_size // 2]

        # Cloning + Mutation
        clones = clone_and_mutate(selected, clone_factor=3, mutation_rate=1.0)

        # Combine and replace
        population = replace(selected + clones, pop_size, lower, upper)

        # Track best
        best = max(population, key=fitness)
        best_history.append(fitness(best))
        print(f"Gen {gen+1}: Best = {best:.4f}, Fitness = {fitness(best):.4f}")

    return population, best_history

# Run Algorithm
pop, history = clonal_selection()
best_solution = max(pop, key=fitness)

print("\nBest Solution:", best_solution)
print("Best Fitness:", fitness(best_solution))

# Plot Convergence
plt.plot(history)
plt.xlabel("Generations")
plt.ylabel("Best Fitness")
plt.title("Clonal Selection Algorithm Convergence")
plt.show()
