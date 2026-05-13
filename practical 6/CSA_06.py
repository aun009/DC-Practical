import numpy as np

def objective(x):
    return -(x[0]**2)  # maximize -x^2 (i.e., find x near 0)

def clone_and_mutate(pop, fitnesses, clone_factor=5, mutate_rate=0.1):
    sorted_idx = np.argsort(fitnesses)[::-1]
    clones = []
    for idx in sorted_idx[:len(pop)//2]:
        n_clones = int(clone_factor * (fitnesses[idx].item() / (np.sum(fitnesses) + 1e-9)))
        for _ in range(max(1, n_clones)):
            clone = pop[idx].copy()
            clone += np.random.normal(0, mutate_rate)
            clones.append(clone)
    return np.array(clones)

def select(pop, fitnesses, pop_size):
    combined = np.vstack([pop, pop])
    combined_fit = np.concatenate([fitnesses, fitnesses])
    best_idx = np.argsort(combined_fit)[::-1][:pop_size]
    return combined[best_idx]

def csa(pop_size=20, dim=1, generations=50):
    pop = np.random.uniform(-10, 10, (pop_size, dim))
    for gen in range(generations):
        fitnesses = np.array([objective(p) for p in pop])
        clones = clone_and_mutate(pop, fitnesses)
        clone_fit = np.array([objective(c) for c in clones])
        pop = select(np.vstack([pop, clones]), np.concatenate([fitnesses, clone_fit]), pop_size)
        best = pop[np.argmax([objective(p) for p in pop])]
        print(f"Gen {gen}: Best={best}, Fitness={objective(best):.4f}")
    return pop[np.argmax([objective(p) for p in pop])]

if __name__ == "__main__":
    best = csa()
    print("Best solution:", best)