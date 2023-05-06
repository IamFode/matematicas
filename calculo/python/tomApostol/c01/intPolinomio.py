"""
1.25 INTEGRACIÓN DE POLINOMIOS
"""

def intPolinomios(a,b,polinomio:str) -> []:
    polinomio = polinomio.replace(' ','') # quitar los space
    terminoActual = ''
    terminos, numeroParentesis = [], 0
    for i in range(len(polinomio)): # Por cada caracter en polinomio
        caracterActual = polinomio[i]
        if i == 0: # El primero caracter, siempre se agrega a terminoActual
            terminoActual = terminoActual + caracterActual
            if polinomio == 'x':
                terminos.append(terminoActual)
        elif i == len(polinomio) - 1: # El ultimo caracter
            terminoActual = terminoActual + caracterActual
            terminos.append(terminoActual)
        else: # Otros caracteres
            if caracterActual == '(': # Si existe parentesis, actualizamos el valor de numeroParentesis
                numeroParentesis += 1
                terminoActual = terminoActual + caracterActual
            elif caracterActual == ')':
                numeroParentesis -= 1
                terminoActual = terminoActual + caracterActual
            elif caracterActual == '+' or caracterActual == '-': # Si se encuentra operador '+' o '-'
                if numeroParentesis > 0: # Si estamos dentro de parentesis
                    terminoActual = terminoActual + caracterActual
                else: # Si estamos fuera de parentesis, crea un nuevo termino
                    terminos.append(terminoActual)
                    terminoActual = caracterActual
            else: # Otros caracteres
                terminoActual = terminoActual + caracterActual
    c,coef,grados,suma = [],[],[],0
    for termino in terminos:
        if "**" in termino:
            grados.append(float(termino.split('**').pop(1).replace('(','').replace(')','')))
        else:
            if 'x' in termino or '+x' in termino:
                grados.append(float(1.0))
            else:
                grados.append(float(0))
        c.append(termino.split('*').pop(0))
    for i in c:
        if i == '+x' or i == 'x':
            coef.append(1.0)
        elif i == '-x':
            coef.append(-1.0)
        else:
            coef.append(float(i))
    for coeficiente,grado in zip(coef,grados):
        suma += coeficiente * ((b**(grado+1)-a**(grado+1))/(grado+1))
    return suma


print(intPolinomios(1,3,'-x+x**2+34*x**2'))

#print(intPolinomios(1,3,'x**(-1)'))

#print(intPolinomios(1,3,'-2*x**(-2)+3*x**(-0.5)+x**3-4+x'))

#print(intPolinomios(1,3,'x**2+4*x**3-2*x**(-2)+3*x**(-0.5)-x**3-42+x-2*x**(-2)+3*x**(-0.5)-x**3-4+x'))



