import numpy as np
import matplotlib.pyplot as plt


# PART D
# Finding the absolute value of DFT(discrete fourier transform) of h4[n], h5[n], h6[n] and h7[n]


# N2 = 4 --> (Question information)
def hFunction(n):
    N = 300
    omega = np.pi / 8
    # When n equals 300, our equation is ambiguous; then, the limit of the equation is 0.125
    if n == 300:
        return 0.125
    if n >= 0 and n <= 2 * N:
        return (np.sin(omega * (n - N))) / (np.pi * (n - N))
    return 0

# h4[n]
def h4Function(n):
    return 2 * np.cos((np.pi / 4) * n) * hFunction(n)


# h5[n]
def h5Function(n):
    return 2 * np.cos((np.pi / 2) * n) * hFunction(n)


# h6[n]
def h6Function(n):
    return 2 * np.cos((3 * np.pi / 4) * n) * hFunction(n)


# h7[n]
def h7Function(n):
    return np.cos((np.pi) * n) * hFunction(n)


# DFT of h3[n]
# K = 1024 --> (Question information)
def DFT(hnFunction, K):
    result = K * [0]
    for k in range(K):
        # Can't define infinite. So declaring scope between -1000 and 1000
        for n in range(-1000, 1000):
            result[k] += hnFunction(n) * np.exp(2j * np.pi * k * n / K)
    return result

out = DFT(h4Function, 1024)
# out = DFT(h5Function, 1024)
# out = DFT(h6Function, 1024)
# out = DFT(h7Function, 1024)
plt.plot(np.abs(out))
plt.show()
