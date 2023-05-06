"""
DEFINICIÓN 1

Una función f es convexa en un intervalo, si para todo a y b del intervalo, el segmento
rectilíneo que une (a, f(a)) y (b, f(b)) se sitúa encima de la gráfica de f.
"""

import matplotlib.pyplot as plt
import numpy as np


def def1(p, q, func, n=13):
    f = lambda x: eval(func)
    x = np.linspace(p, q, 100)
    fig, ax = plt.subplots()
    ax.plot(x, f(x)) # trazar la función completa
    line = np.linspace(p, q, n) # puntos de la recta
    last_line = None # variable para guardar la última línea trazada
    for idx,a in enumerate(line):
        for b in line:
            if not a == b:
                for xx in np.linspace(a, b, n):
                    gx = ((f(b)-f(a))/(b-a))*(xx-a)+f(a) 
                    if gx>f(xx) and a<xx<b:
                        if last_line: # si hay una línea trazada anteriormente, borrarla
                            last_line.remove()
                        current_line, = ax.plot([a, b], [f(a), f(b)], color=plt.cm.jet(idx / len(line)), alpha=.9) # guardar la línea actual
                        last_line = current_line # guardar la línea actual como la última línea trazada
                        plt.pause(0.001)
    return plt.show()

# Funciona sólo para una única curva.
def1(-10, 10, 'x**2')
