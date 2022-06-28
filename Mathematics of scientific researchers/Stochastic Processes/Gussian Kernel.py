import numpy as np


def gaussian_kernel(x1, x2, lv=1.0, sigma=1.0):

    m = x1.shape[0]
    n = x2.shape[0]
    dist_matrix = np.zeros((m, n), dtype=float)
    for i in range(m):
        for j in range(n):
            dist_matrix[i][j] = np.sum((x1[i] - x2[j]) ** 2)

    return sigma ** 2 * np.exp(- 0.5 / lv ** 2 * dist_matrix)


def gussian_kernel_vectorization(x1, x2, lv=1.0, sigma=1.0):

    dist_matrix = np.sum(x1**2, 1).reshape(-1,1) + np.sum(x2**2,1) - 2 * np.dot(x1, x2.T)

    return sigma ** 2 * np.exp(- 0.5 / lv ** 2 * dist_matrix)


x = np.array([700, 800, 1029]).reshape(-1, 1)

kernel = gaussian_kernel(x, x, lv=500, sigma=10)
print(kernel)

kernel_vec = gussian_kernel_vectorization(x, x, lv=500, sigma=10)
print(kernel_vec)
