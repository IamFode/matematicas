import matplotlib.pyplot as plt 
import numpy as np

# gráfica de desplazamiento de funciones
x = np.arange(-15, 15, 0.01)
y, y1, y2 = -x**2, -(x+7)**2, -(x-4)**2
fig, ax = plt.subplots()
ax.plot(x,y)
ax.plot(x, y1)
ax.plot(x, y2)
ax.set(xlabel='x', ylabel='y',
       title='Desplazamiento de funciones')
ax.grid
plt.show()
