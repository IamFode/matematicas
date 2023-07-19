"""
Definición 1.5_

Estas tres propiedades deben complementarse con las siguientes definiciones.

\begin{tabular}{rcl}
$a>b$&si&$a-b$ pertenece a $P$\\
$a<b$&si&$b>a$\\
$a\geq b $&si&$a>b$ ó $a=b$\\
$a\leq b$&si&$a<b$ ó $a=b$\\
\end{tabular}

Nótese en particular que $a>0$ si y sólo si $a$ pertenece a $P$.
"""

def def1_5(a,b):
    if a-b>0:
        return"{0}>{1} si {0}-{1} pertenece a P".format(a,b)
    if b>a:
        return"{0}<{1} si {1}>{0}".format(a,b)
    if a>=b:
        return"{0}>={1} si {0}>{1} o {0}={1}".format(a,b)
    if a<=b:
        return"{0}<={1} si {0}<{1} o {0}={1}".format(a,b)
print(def1_5(2,0))

