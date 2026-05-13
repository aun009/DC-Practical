import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor

# Data
X = np.random.rand(100, 2)
y = 0.8 * X[:,0] + 0.5 * X[:,1] + np.random.rand(100) * 0.1
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2)

# GA population [neurons, lr]
pop = [[random.randint(5,50), random.uniform(0.001,0.1)] for _ in range(10)]

def fitness(ind):
    n, lr = ind
    m = MLPRegressor(hidden_layer_sizes=(n,), learning_rate_init=lr, max_iter=200)
    m.fit(Xtr, ytr)
    return mean_squared_error(yte, m.predict(Xte))

# GA loop
for _ in range(5):
    pop = sorted(pop, key=fitness)[:5]
    while len(pop) < 10:
        p1, p2 = random.sample(pop, 2)
        child = [random.choice([p1[0], p2[0]]), random.choice([p1[1], p2[1]])]
        if random.random() < 0.1:
            child[0] = random.randint(5, 50)
        if random.random() < 0.1:
            child[1] = random.uniform(0.001, 0.1)
        pop.append(child)

best = min(pop, key=fitness)
print("Best Parameters:", best)

# Final model
model = MLPRegressor(hidden_layer_sizes=(best[0],), learning_rate_init=best[1], max_iter=300)
model.fit(Xtr, ytr)
pred = model.predict(Xte)
print("Final MSE:", mean_squared_error(yte, pred))

# Plot
plt.scatter(yte, pred)
plt.plot([min(yte), max(yte)], [min(yte), max(yte)])
plt.xlabel("True Values")
plt.ylabel("Predicted Values")
plt.title("GA-NN Optimization")
plt.show()

