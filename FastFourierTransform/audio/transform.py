import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read, write
from time import time
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('falta el archivo')
        exit()

    archivo = sys.argv[1]
    if not os.path.isfile(archivo):
        print('no existe')
        exit()

    print('leyendo %s'%archivo)

    rate, signal = read(archivo)

    print('rate: %d'%rate)

    print('calculando la transformada...')
    t_ini = time()
    transformada = np.fft.fft(signal)
    t_fin = time()

    print('se obtuvo la transformada en %.2f segundos'%(t_fin-t_ini))

    fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True)

    ax0.set_title('Audio')
    ax0.plot(signal)

    ax1.set_title('Transform')
    ax1.plot(transformada)

    plt.show()

    print('escribiendo archivo...')

    nombre = archivo.split('.')[0]

    write(nombre + '_transformada.wav', rate, np.array([
        np.abs(i)
        for i in transformada
    ], dtype=np.int16))

    # Creación de una imagen a partir de la transformada
