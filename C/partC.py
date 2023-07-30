import numpy as np
import matplotlib.pyplot as plt


# PART C
# Finding the absolute value of DFT(discrete fourier transform) of h3[n]


# h3[n] = sin omega(n - N2)/pi(n - N2) if 0 <= n <= 2 * N2 & else 0
# N1 = 4 --> (Question information)
def h3Function(n, N2, omega):
    # When n equals 300, our equation is ambiguous; then, the limit of the equation is 0.125
    if n == 300:
        return 0.125
    if n >= 0 and n <= 2 * N2:
        return (np.sin(omega * (n - N2))) / (np.pi * (n - N2))
    return 0

# DFT of h3[n]
# K = 1024 --> (Question information)
def DFT(h3Function, K):
    result = []
    for i in range(K):
        result += [0]
    for k in range(K):
        # Can't define infinite. So declaring scope between -1000 and 1000
        for n in range(-1000, 1000):
            result[k] += h3Function(n, 300, np.pi / 8) * np.exp(2j * np.pi * k * n / K)
    return result


out = DFT(h3Function, 1024)
plt.plot(np.abs(out))
plt.show()
