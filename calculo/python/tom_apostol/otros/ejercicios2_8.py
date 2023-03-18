import math
import numpy as np

class ej2_8:

    def __init__(self,*args):
        self.args = args

    #problema 1 inciso (a)
    def problem1a(self):
        return math.sin(self.n*math.pi)
    
    # problema 17 de la a hasta la h
    def problem17(self,num2):
        return -(math.cos(self.num2)-math.cos(self.num1))

    # problema 28
    def problem28a(self,a,b):
        # formula para la integral de la función sen(a+bx) 
        return (1/self.b)*(math.sin(self.a+self.b*self.x))





