import numpy as np

def plane_tone(freq, rate, i):
    return (-1)**int(i / rate * 2 * freq)

def sin_tone(freq, rate, i):
    return np.sin(2*np.pi*i*freq/rate)

# decays
def exp_decay(rate, i):
    return np.exp(-i/(rate/5))

def linear_decay(rate, i):
    return 1 - i/rate

def square_decay(rate, i):
    return np.sqrt(rate - i)/np.sqrt(rate)

def poly_decay(rate, i):
    x = 1 - i/rate
    return x**5