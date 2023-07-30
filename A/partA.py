import numpy as np
import matplotlib.pyplot as plt


# Part A
# Finding the absolute value of DFT(discrete fourier transform) of h1[n]


# h1[n] = 1 if 0 <= n <= 2 * N1 & else 0
# N1 = 4 --> (Question information)
def h1Function(n, N1):
    if n >= 0 and n <= 2 * N1:
        return 1
    else:
        return 0


# DFT of h1[n]
# K = 1024 --> (Question information)
def DFT(h1Function, K):
    result = []
    for i in range(K):
        result += [0]
    for k in range(K):
        # Can't define infinite. So declaring scope between -1000 and 1000
        for n in range(-1000, 1000):
            result[k] += h1Function(n, 4) * np.exp(2j * np.pi * k * n / K)
    return result


out = DFT(h1Function, 1024)
plt.plot(np.abs(out))
plt.show()