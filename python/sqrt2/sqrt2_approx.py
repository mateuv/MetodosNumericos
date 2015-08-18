# Pasar por línea de comandos el número de cifras deseadas:
#
# $ python tarea_2.4.py 1000
#
# Adicionalmente se puede pedir comparación del número con otro de 5 millones de
# cifras que está en el archivo sqrt2.txt usando:
#
# $ python tarea_2.4.py 1000 --check
#
# Este programa se basa en la aproximación por el método de babilonia de la raíz
# cuadrada de un número, en el que se usa una aproximación inicial y se construye
# a partir de ella una serie que converge al número buscado.
#
# Python 3.4.2, using gmpy
from math import log, ceil
from gmpy2 import mpz
import sys

def babilon_approx(n, first_guess):
	next_aprox = first_guess
	while True:
		yield next_aprox
		next_aprox = (next_aprox + n//next_aprox)//2

if __name__ == '__main__':
	number_of_digits_desired = int(sys.argv[1]) if len(sys.argv)>1 else 80
	iterations               = ceil(log(number_of_digits_desired, 2))
	base                     = 2*mpz(100)**number_of_digits_desired
	first_guess              = (14*mpz(100)**(number_of_digits_desired//2))//10
	aprox                    = babilon_approx(base, first_guess)

	# Consume iterator
	for i in range(iterations-1): next(aprox)

	number = str(next(aprox))
	number = '1.'+number[1:]

	c = 'x'

	if '--check' in sys.argv:
		with open('sqrt2.txt', 'r') as basefile:
			for index, letter in enumerate(number):
				while c not in '0123456789.':
					c = basefile.read(1)
				if c != letter:
					print ('Falló en el indice %d'%index)
					break
				c = basefile.read(1)
			else:
				print ('El número es bueno!')
	else:
		print (number)
