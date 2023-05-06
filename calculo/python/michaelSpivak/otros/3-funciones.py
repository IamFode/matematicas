# Problemas 

class Funciones():

    def __init__(self): 
    '''problema 1.'''
        pass
    '''(i)'''
    def func1i(self,x):
        if x != 1 or x!=-2:
            return 1/(1+(1/1+x)) 
        else:
            return 'no es correcto'
    '''(ii)'''
    def func1ii(self,x):
        if x != -1 or x != 0:   
            return 1/(1/(1+x))
        else:
            return 'no es correcto'
    '''(iii)'''
    def func1iii(self,x,c):
        if x != -1 and c !=0:
            return 1/(1+x*c)
        else:
            return 'no es correcto'
    '''(iv)'''
    def func1iv(self,x,y):
        if (x+y) != -1:
            return 1/(1+x+y)
        else:
            return 'no es correcto'
    '''(v)'''
    def func1v(self,x,y):
        if x != -1 and y != -1:
            return (x+y+2)/(1+x)*(1+y)
        else:
            return 'no es correcto'

funciones = Funciones()

print(funciones.func1i(2))
