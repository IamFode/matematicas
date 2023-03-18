import numpy as np

def convexa(x,y,i):
    if x<y and i<1 and i>0:
        def g(x):
            return x**3 
        for a in np.arange(i,1,i):
            z = a*y + (1-a)*x
            z2 = a*g(y)+(1-a)*g(x)
            if g(z) <= z2:
                print("Para alfa = {:.2f}, {:.2f} <= {:.2f}".format(a,g(z),z2))
            else:
                print("Para alfa = {:.2f}, {:.2f} >= {:.2f}".format(a,g(z),z2))
    else:
        print("ingrese x<y y 0<i<1")

convexa(-3,-1,0.1)
