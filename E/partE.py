import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write


# h3[n]
def h3(n):
    N = 300
    omega = np.pi / 8
    if n == 300:
        return 0.125
    if n >= 0 and n <= 2 * N:
        return (np.sin(omega * (n - N))) / (np.pi * (n - N))
    return 0


# h4[n]
def h4(n):
    return 2 * np.cos((np.pi / 4) * n) * h3(n)


# h5[n]
def h5(n):
    return 2 * np.cos((np.pi / 2) * n) * h3(n)


# read the wav file
rate, data = wavfile.read('test.wav')


# create the arrays for the responses
h3Responses = np.zeros(data.shape[0])
h4Responses = np.zeros(data.shape[0])
h5Responses = np.zeros(data.shape[0])


# calculate the responses
for i in range(len(data)):
    h3Responses[i] = h3(i)
    h4Responses[i] = h4(i)
    h5Responses[i] = h5(i)


# convolve the data with the responses
resH3 = np.convolve(data, h3Responses)
resH4 = np.convolve(data, h4Responses)
resH5 = np.convolve(data, h5Responses)


# write the results to wav files
write("res(h3).wav", rate, resH3)
write("res(h4).wav", rate, resH4)
write("res(h5).wav", rate, resH5)


