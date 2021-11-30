import random as rd
import pandas as pd

iris = r.iris
iris.head()
############# Random sample
rows = rd.sample(range(0,150),5)
iris.iloc[rows,:]
iris.sample(frac=0.02)
