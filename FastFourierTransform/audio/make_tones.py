import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from tones import sin_tone, exp_decay

if __name__ == '__main__':
    RATE = 48000

    MAX_VOL = 15000

    FREQ = 440 # * 2**(1/4)

    MOD = int(RATE / (2 * FREQ))

    signal = np.array([
        sin_tone(FREQ, RATE, i) * MAX_VOL * exp_decay(RATE, i)
        for i in range(RATE)
    ])

    FREQ = 440 * 2**(1/3)
    MOD = RATE / FREQ

    # signal += np.array([
    #     (-1)**(i//int(MOD)) * MAX_VOL * np.exp(-i/(RATE/5))
    #     for i in range(RATE)
    # ])

    # signal = np.concatenate((signal, signal2))

    plt.plot(signal)

    plt.show()

    wavfile.write('made.wav', RATE, np.array(signal, dtype=np.int16))
