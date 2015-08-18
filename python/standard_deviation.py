# Calcula la desviación estándar de un conjunto de datos respecto a una función
# dada
import numpy as np
from math import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
from functools import partial

def deviation(f, x_data, y_data):
    S = sum(map(lambda x, y:(f(x) - y)**2, x_data, y_data))
    return sqrt(S/4)

if __name__ == '__main__':
    def f(x, a, b):
        return a*sin(x*pi/2) + b*cos(x*pi/2)

    g = partial(f, a=3.0802, b=-2.0285)

    x_data = [-.5, -.19, .02, .2, .35, .5]
    y_data = [-3.558, -2.874, -1.995, -1.04, .068, .677]

    x = np.linspace(-1, 1, 100)
    y = list(map(g, x))

    plt.plot(x, y, '-', x_data, y_data, 'o')
    plt.show()

    # Compute standard deviation

    desviacion = deviation(g, x_data, y_data)

    print("desviación estándar:", desviacion)
