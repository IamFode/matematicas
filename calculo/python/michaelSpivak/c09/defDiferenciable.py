"""
La función f es diferenciable en a si existe el
lim_{h\to 0} \dfrac{f(a+h)-f(a)}{h}.
En este caso, dicho límite  se representa mediante f'(a) y se denomina la derivada de f en a.
(Diremos también que f es diferenciable en a para todo a del dominio de f.)
"""

def diferenciable(func, a, h):
    f = lambda x: eval(func)
    lim = (f(a+h)-f(a))/h
    return lim

def diferenciableBool(func,a,h):
    def f(x):
        try:
            return eval(func)
        except:
            return None
    if f(a) is None or f(a+h) is None:
        return None
    elif h == 0:
        return None
    else:
        try:
            f = lambda x: eval(func)
            lim = (f(a+h) - f(a)) / h
            return lim is not None and not isinstance(lim, str) and not isinstance(lim, bool)
        except:
            return False

