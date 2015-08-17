import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

if __name__ == '__main__':
    rate, signal = wavfile.read('voces.wav')

    print('rate: %d'%rate)

    fourier = np.fft.fft(signal)

    n = signal.size

    timestep = 0.1

    freq = np.fft.fftfreq(n, d=timestep)

    plt.plot(freq)
    plt.show()

    print(freq)
