import matplotlib.pyplot as plt
import numpy as np

# Desplazamiento de funciones
x = np.arange(-5,5,0.01)
y, y1, y2 = x**2, x**2 + 3, x**2 - 5
fig,ax = plt.subplots()
ax.plot(x,y,label="$y=x^2$")
ax.plot(x,y1,label="$y=x^2 + 3$")
ax.plot(x,y2,label="$y=x^2-5$")
ax.legend(fontsize="xx-small")
ax.set(xlabel="x", ylabel="y", title = "Desplazamiento")
ax.grid
plt.show()
