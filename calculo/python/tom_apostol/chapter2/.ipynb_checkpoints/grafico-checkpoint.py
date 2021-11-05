import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()


def ejercicios24(a,b,fx,gx):
    x = np.arange(a,b,0.01)
    f = fx 
    g = gx
    fig, ax = plt.subplots()
    ax.plot(x,f)
    ax.plot(x,g)
    ax.set(xlabel = "x", ylabel="f(x)",title="Integrales")
    ax.legend()
    plt.show()

