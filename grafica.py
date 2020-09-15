import numpy as np

import matplotlib.pylab as plt

x = np.linspace(-1, 1, 50)

y1 = 2*x

y2 = 2*(x)**2 + 1

y3 = 2*(x)**3 - 2

plt.figure(num='MiPrimerGrafico')
Out[41]: <Figure size 432x288 with 0 Axes><Figure size 432x288 with 0 Axes>

plt.plot(x, y1)
Out[42]: [<matplotlib.lines.Line2D at 0x2d4340f89a0>]
￼
