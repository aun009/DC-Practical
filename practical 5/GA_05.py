import numpy as np
from sklearn.neural_network import MLPRegressor

# Dummy dataset: [inlet_temp, feed_flow, airflow] -> moisture_content
X = np.random.rand(100, 3)
y = np.random.rand(100)

def fitness(params):
    hidden = int(params[0])
    lr = max(0.0001, params[1])
    nn = MLPRegressor(hidden_layer_sizes=(hidden,), learning_rate_init=lr, max_iter=500)
    nn.fit(X, y)
    pred = nn.predict(X)
    return -np.mean((pred - y)**2)  # negative MSE (GA maximizes)

# GA parameters to optimize: [hidden_neurons, learning_rate]
population = np.random.rand(20, 2)
population[:,0] = np.clip(population[:,0]*50, 1, 100)
population[:,1] = np.clip(population[:,1]*0.1, 0.0001, 0.1)

for gen in range(10):
    scores = np.array([fitness(ind) for ind in population])
    best = population[np.argmax(scores)]
    print(f"Gen {gen}: Best fitness={max(scores):.4f}, params={best}")
    # Selection, crossover, mutation (simplified)
    parents = population[np.argsort(scores)[-5:]]
    offspring = []
    for _ in range(len(population)-5):
        p1, p2 = parents[np.random.choice(5, 2, replace=False)]
        child = (p1 + p2)/2 + np.random.normal(0, 0.1, 2)
        child[0] = np.clip(child[0], 1, 100)
        child[1] = np.clip(child[1], 0.0001, 0.1)
        offspring.append(child)
    population = np.vstack([parents, offspring])