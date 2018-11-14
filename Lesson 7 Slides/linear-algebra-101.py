
# coding: utf-8



get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from scipy.linalg import lu


# ## Basic Matrix Syntax

# ### Initializing a 2x2 matrix



matrix = np.array([[2,-1],[1,-2]])
print(matrix)


# ### Transposing matrix



print(matrix.transpose())


# ### Matrix multiplication



A = np.array([[1,1],[0,0]])
B = np.array([[0,0],[2,0]])
AB = np.dot(A,B)
print(AB)


# ### Determinant of matrix



detMatrix = np.linalg.det(matrix)
print(detMatrix)


# ### Inverse of matrix



invMatrix = np.linalg.inv(matrix)
print(invMatrix)


# ### Example of solving a system of linear equations
# - 2 methods:
#     - get inverse and matrix multiplication
#     - solve with innate function

# #### Solve with innate function



example_matrix = np.array([[2,-1],[1,-2]])
example_numeric = np.array([[6],[3]])
np.linalg.solve(example_matrix, example_numeric)


# #### Solve with inverse and matrix multiplication



np.dot(np.linalg.inv(example_matrix),example_numeric)


# ## Basic Vectors/Spaces Syntax

# ### Initializing a vector



vector = np.array([1,2,3])
print(vector)


# ### Inner product of 2 vectors



a = np.array([1,2,3])
b = np.array([0,1,0])
np.inner(a, b)


# ### Norm of a vector



np.linalg.norm(a)


# ### Euclidean distance of 2 vectors



np.linalg.norm(a-b)


# ## Eigen values and vectors



matrix = np.array([[11,1],[1,11]])
print(np.linalg.eig(matrix))


# ### Orthogonal vectors
# - gram schmidt process
# - we can reference from QR decomposition, where Q is the orthonormal set



A = np.array([[1,0,0], [1,1,0], [1,1,1]])
q, r = np.linalg.qr(A)
q


# ### Singular Value Decomposition (SVD)
# - same example in slide



svd_matrix = np.array([[3,1,1],[-1,3,1]])




u, s, v = np.linalg.svd(svd_matrix, full_matrices=True)




print(u)




print(s)




print(v)


# ### Principal Component Analysis (PCA)



example_matrix = np.array([[1,1,2,0,5,4,5,3],[3,2,3,3,4,5,5,4]])
pca = PCA()




pca.fit(example_matrix)




plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')




pca = PCA(n_components=1)
pca.fit(example_matrix)




pca.components_


# ### LU Decomposition



lu_example = np.array([[3,1],[-6,-4]])

p,l,u = lu(lu_example)




p




l




u

