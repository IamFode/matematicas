from matplotlib import pyplot as plt
import numpy as np
x=np.linspace(-1,1,1000)
plt.style.use('ggplot')
plt.plot(x,-x**2 + 1)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
