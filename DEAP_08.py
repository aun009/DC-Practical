import random
from deap import base, creator, tools, algorithms

# Define Fitness & Individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox Setup
toolbox = base.Toolbox()

# Attribute: random number between -10 and 10
toolbox.register("attr_float", random.uniform, -10, 10)

# Individual & Population
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness Function
def fitness(ind):
    x = ind[0]
    return (x**2,)

toolbox.register("evaluate", fitness)

# Genetic Operators
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run Algorithm
pop = toolbox.population(n=10)
algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=10, verbose=True)

# Best Solution
best = tools.selBest(pop, 1)[0]
print("\nBest Solution:", best[0])
print("Best Fitness:", fitness(best)[0])
