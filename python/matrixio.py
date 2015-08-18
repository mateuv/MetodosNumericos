# Entrada/salida de matrices a/desde archivos de texto
# Las entradas de la matriz pueden contener literales y funciones matemáticas
# básicas
import math
import numpy as np
from pprint import pprint
from functools import partial
import sys

"""
Leer matrices de un archivo y devolverlas como matrices de numpy
"""

# lista de funciones matemáticas disponibles
mathprops = {i:getattr(math, i) for i in dir(math)}

def matheval(expr):
    "permite evaluar literales y funciones matemáticas"
    try:
        return eval(expr, mathprops)
    except:
        return 0

def read(path):
    with open(path, 'r') as fd:
        return np.array([np.array(list(map(matheval, filter(
            lambda x: x,
            row
            .strip()
            .split(' '))))) for row in fd.readlines()])

def write(matrix, path):
    with open(path, 'w') as fd:
        fd.writelines((' '.join(map(str, row))+'\n' for row in matrix))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("falta un parámetro")
        exit()

    matrix = read(sys.argv[1])
    print (matrix)
    # write(matrix, 'write.txt')
