"""
DEFINICIÓN 1

Una función f es convexa en un intervalo, si para todo a y b del intervalo, el segmento
rectilíneo que une (a, f(a)) y (b, f(b)) se sitúa encima de la gráfica de f.
"""

import matplotlib.pyplot as plt
import numpy as np

def def1(p, q, func, n):
    f = lambda x: eval(func)
    x = np.linspace(p, q, 100)
    fig, ax = plt.subplots()
    ax.plot(x, f(x)) # trazar la función completa
    line = np.linspace(p, q, n) # puntos de la recta
    for a in line:
        for b in line:
            if not a == b:
                for xx in np.linspace(a, b, n):
                    gx = ((f(b)-f(a))/(b-a))*(xx-a)+f(a) 
                    if gx>f(xx) and a<xx<b:
                        ax.plot([a, b], [f(a), f(b)], color='blue', alpha=.9)
                        plt.pause(.1)

    return plt.show()

#ax.plot([i, j], [f(i), f(j)], color=plt.cm.jet(idx / len(line)), alpha=.9)


# Funciona sólo para una única curva.
def1(0, 10, 'x**3+x', 10)
