import numpy as np
from scipy.integrate import quad

f = lambda x: np.sin(x) - np.cos(x) 
area = quad(f,0,np.pi/2)

print(area)
