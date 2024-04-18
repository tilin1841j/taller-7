
import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def calculate_eigen(self):
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
        return eigenvalues, eigenvectors

# Example usage:
M = Matrix(np.array([[1, 2, 5], [2, 3, 5], [10, 15, 9] ]))
eigenvalues, eigenvectors = M.calculate_eigen()
print("valores propios:")
print(eigenvalues)
print("vectores propios:")
print(eigenvectors)

