import numpy as np

print("== BASICS ==")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Dot Product:", np.dot(a, b))

print("Scalar Operations: a * 2 =", a * 2)

print("Slicing:", a[1:])        # [2 3]
print("Boolean Indexing:", a[a > 1])  # [2 3]

print("\n== MATRIX OPERATIONS ==")
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A + B:\n", A + B)
print("A * B (element-wise):\n", A * B)
print("A @ B (matrix multiplication):\n", A @ B)
print("Transpose of A:\n", A.T)
print("Inverse of A:\n", np.linalg.inv(A))

print("\n== STATISTICS ==")
data = np.array([10, 20, 20, 40, 50])

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("25th Percentile:", np.percentile(data, 25))
print("75th Percentile:", np.percentile(data, 75))

print("\n== LINEAR ALGEBRA ==")
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solving Ax = b
x = np.linalg.solve(A, b)
print("Solving Ax = b:", x)

# Determinant
print("Determinant of A:", np.linalg.det(A))

# Eigenvalues and Eigenvectors
eig_vals, eig_vecs = np.linalg.eig(A)
print("Eigenvalues:", eig_vals)
print("Eigenvectors:\n", eig_vecs)