import numpy as np

def fuzzy_union(A, B):
    return {k: max(A.get(k, 0), B.get(k, 0)) for k in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {k: min(A.get(k, 0), B.get(k, 0)) for k in set(A) & set(B)}

def fuzzy_complement(A):
    return {k: 1 - v for k, v in A.items()}

def fuzzy_difference(A, B):
    return {k: min(A.get(k, 0), 1 - B.get(k, 0)) for k in A}

def cartesian_product(A, B, method='min'):
    A_items = sorted(A.items())
    B_items = sorted(B.items())
    R = np.zeros((len(A_items), len(B_items)))
    for i, (x, muA) in enumerate(A_items):
        for j, (y, muB) in enumerate(B_items):
            R[i][j] = min(muA, muB) if method == 'min' else muA * muB
    return R, [x for x,_ in A_items], [y for _,y in B_items]

def max_min_composition(A_vector, R_matrix):
    A = np.array([A_vector])
    B = np.zeros(A.shape[1])
    for j in range(R_matrix.shape[1]):
        B[j] = max([min(A[0][i], R_matrix[i][j]) for i in range(R_matrix.shape[0])])
    return B

# Example usage
if __name__ == "__main__":
    A = {'x1': 0, 'x2': 1, 'x3': 0.7, 'x4': 0.4, 'x5': 0.2, 'x6': 0}
    B = {'x1': 0, 'x2': 0.4, 'x3': 0.7, 'x4': 0.8, 'x5': 1, 'x6': 0}
    
    print("Union:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement A:", fuzzy_complement(A))
    print("Difference A-B:", fuzzy_difference(A, B))
    
    A2 = {'1': 1, '2': 0.8, '3': 0.6, '4': 0.5}
    B2 = {'1': 0.5, '2': 1, '3': 0.3, '4': 0}
    R, _, _ = cartesian_product(A2, B2, 'min')
    print("Cartesian Product (R):\n", R)
    
    A_vec = [0.9, 0.4, 0]
    R2 = np.array([[1, 0.8, 0.1], [0.8, 0.6, 0.3], [0.6, 0.3, 0.1]])
    print("Max-Min Composition:", max_min_composition(A_vec, R2))