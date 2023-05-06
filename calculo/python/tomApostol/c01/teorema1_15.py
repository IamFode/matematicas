"""
Si p es un entero positivo y b>0, tenemos
int_0^b x^p dx = b^(p+1)/(p+1). 
"""

def teo1_15(b,p): 
    if p%1==0 and p>0 and b>0: # p entero positivo y b>0
        return b**(p+1)/(p+1) # int_0^b x^p dx = b^(p+1)/(p+1)
    else:
        print("b debe ser positivo")
