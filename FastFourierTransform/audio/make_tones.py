import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read, write
from time import time
import sys
import os

if __name__ == '__main__':
    RATE = 48000

    MAX_VOL = 15000

    FREQ = 440 # * 2**(1/4)

    MOD = int(RATE / FREQ)

    signal = np.array([
        (-1)**(i//MOD) * MAX_VOL * np.exp(-i/(RATE/5))
        for i in range(RATE)
    ])

    FREQ = 440 * 2**(1/3)
    MOD = RATE / FREQ

    signal += np.array([
        (-1)**(i//int(MOD)) * MAX_VOL * np.exp(-i/(RATE/5))
        for i in range(RATE)
    ])

    # signal = np.concatenate((signal, signal2))

    plt.plot(signal)

    plt.show()

    write('made.wav', RATE, np.array(signal, dtype=np.int16))
