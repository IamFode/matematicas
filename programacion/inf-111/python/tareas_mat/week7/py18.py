import numpy as np
from scipy.integrate import quad

f = lambda x: x + np.sin(x) 
area = quad(f,0,np.pi)

print(area)
