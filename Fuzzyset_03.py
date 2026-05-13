# Fuzzy Set Operations
def union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def complement(A):
    return {x: 1 - A[x] for x in A}

def difference(A, B):
    return {x: min(A.get(x, 0), 1 - B.get(x, 0)) for x in set(A) | set(B)}

# Cartesian Product (Fuzzy Relation)
def cartesian_product(A, B):
    return {(x, y): min(A[x], B[y]) for x in A for y in B}

# Max-Min Composition
def max_min_composition(R, S):
    T = {}
    for (x, y1), val1 in R.items():
        for (y2, z), val2 in S.items():
            if y1 == y2:
                value = min(val1, val2)
                T[(x, z)] = max(T.get((x, z), 0), value)
    return T

# Example Fuzzy Sets
A = {'a': 0.2, 'b': 0.7, 'c': 1.0}
B = {'a': 0.5, 'b': 0.4, 'c': 0.9}

# Display Input Sets
print("===== FUZZY SETS =====")
print("Set A:")
for k, v in A.items():
    print(f"  {k} : {v}")

print("\nSet B:")
for k, v in B.items():
    print(f"  {k} : {v}")

# Operations
print("\n===== OPERATIONS =====")
print("Union (A U B):", union(A, B))
print("Intersection (A n B):", intersection(A, B))
print("Complement of A:", complement(A))
print("Difference (A - B):", difference(A, B))

# Relations
R = cartesian_product(A, B)
S = cartesian_product(B, A)

print("\n===== RELATIONS =====")
print("Relation R (A x B):")
for k, v in R.items():
    print(f"  {k} : {v}")

print("\nRelation S (B x A):")
for k, v in S.items():
    print(f"  {k} : {v}")

# Composition
T = max_min_composition(R, S)

print("\n===== MAX-MIN COMPOSITION =====")
for k, v in T.items():
    print(f"  {k} : {v}")
  
