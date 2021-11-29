import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5,0.01)
y1, y2, y3, y4 = (x-1)**2 - 4, (x-2)**2 + 2, (x+2)**2 + 2, (x+3)**2 - 2
fig,ax = plt.subplots()
ax.plot(x,y1,label="$y=(x-1)**2 - 4$")
ax.plot(x,y2,label="$y=(x-2)^2 + 2$")
ax.plot(x,y3,label="$y=(x+2)^2 + 2$")
ax.plot(x,y4,label="$y=(x+3)^2 - 2$")
ax.legend(fontsize="xx-small")
ax.set(xlabel="x",ylabel="y",title="Desplazamiento")
ax.grid
plt.show()
