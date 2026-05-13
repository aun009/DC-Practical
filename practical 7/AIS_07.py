import numpy as np
import random
import matplotlib.pyplot as plt

# Generate Dummy Structural Data
np.random.seed(42)
X = np.random.rand(100, 3) # features
y = (X[:,0] + X[:,1] > 1).astype(int) # damage classification

# Split data
split = 80
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Antibody (Model)
def create_antibody():
    return np.random.rand(3) # weights

def predict(ab, x):
    return 1 if np.dot(ab, x) > 1.5 else 0

# Fitness (Accuracy)
def fitness(ab):
    correct = sum(predict(ab, x) == y for x, y in zip(X_train, y_train))
    return correct / len(X_train)

# Clone + Mutate
def clone_mutate(pop):
    clones = []
    for i, ab in enumerate(pop):
        for _ in range(3):
            mutation = np.random.uniform(-0.1/(i+1), 0.1/(i+1), size=3)
            clones.append(ab + mutation)
    return clones

# AIS Training
pop = [create_antibody() for _ in range(10)]
history = []

for gen in range(20):
    pop = sorted(pop, key=fitness, reverse=True)
    best = pop[:5]
    clones = clone_mutate(best)
    pop = best + clones
    
    # Replace worst
    pop += [create_antibody() for _ in range(5)]
    best_fit = fitness(pop[0])
    history.append(best_fit)
    print(f"Gen {gen+1} Accuracy: {best_fit:.2f}")

# Test Best Model
best_ab = max(pop, key=fitness)
test_acc = sum(predict(best_ab, x) == y for x, y in zip(X_test, y_test)) / len(X_test)
print("\nTest Accuracy:", test_acc)

# Plot Accuracy
plt.plot(history)
plt.xlabel("Generations")
plt.ylabel("Accuracy")
plt.title("AIS Damage Classification")
plt.show()
