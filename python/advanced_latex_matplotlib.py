# Ejemplo avanzado del uso de latex en una gráfica de matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['text.latex.unicode'] = True
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = '\\usepackage{amsthm}', '\\usepackage{amsmath}', '\\usepackage{amssymb}',
'\\usepackage{amsfonts}', '\\usepackage[T1]{fontenc}', '\\usepackage[utf8]{inputenc}, \\usepackage{multicol}'
rcParams['legend.handleheight'] = 3.0

def f(x):
	return np.piecewise(x, [x < 0, x == 0, x > 0], [-2, 0, 2])

if __name__ == '__main__':
	x = np.linspace(-1, 1, 100)

	fig = plt.figure()

	plt.plot(x, f(x), 'bo', [0], [0], 'bo')

	plt.title('$f(x)=\\left\\{\\begin{array}{lr} -2 & : x<0\\\\ 0 & : x=0\\\\ 2 & : x>0\\end{array}\\right\\}$')

	fig.text(0.5, 0.75, 'Continua en todo $\\mathcal{R}-\phi$', ha='center')

	plt.show()
