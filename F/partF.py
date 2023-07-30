import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write


# h3[n]
def h3(n):
    N = 300
    omega = np.pi / 8
    if n == 300:
        return 0.125
    if 2 * N >= n >= 0:
        return (np.sin(omega * (n - N))) / (np.pi * (n - N))
    return 0

# h4[n]
def h4(n):
    return 2 * np.cos((np.pi / 4) * n) * h3(n)

# h5[n]
def h5(n):
    return 2 * np.cos((np.pi / 2) * n) * h3(n)

# equalizer1[n]
def equalizer1(n):
    return 5 * h3(n) + h4(n) + (1 / 3) * h5(n)

# equalizer2[n]
def equalizer2(n):
    return (1 / 3) * h3(n) + h4(n) + 5 * h5(n)

# read wav file
rate, data = wavfile.read('test.wav')

# equalizer
equalizerResponse1 = np.zeros(data.shape[0])
equalizerResponse2 = np.zeros(data.shape[0])

# calculate equalizer response
for i in range(len(data)):
    equalizerResponse1[i] = equalizer1(i)
    equalizerResponse2[i] = equalizer2(i)

# calculate equalizer result
equalizerResult1 = np.convolve(equalizerResponse1, data)
equalizerResult2 = np.convolve(equalizerResponse2, data)

# write wav file
write("res(equalizer1).wav", rate, equalizerResult1)
write("res(equalizer2).wav", rate, equalizerResult2)
