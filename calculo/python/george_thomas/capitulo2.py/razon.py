#definición de razón promedio de cambio

def rpc(x1,x2):
    fx = exec(input())
    f = lambda x: fx 
    rpc = (f(x1) - f(x2)) / (x2 - x1) 

rpc(2,4)

