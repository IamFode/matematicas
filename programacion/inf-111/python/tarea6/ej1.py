
N = int(input("tamaño de la población: "))
while N<=1 and N>=100: 
    N = int(input("tamaño de la población: "))

T = int(input("tamaño de la tabla de densidad: "))
while T<=1 and T>=100: 
    T = int(input("tamaño de la tabla de densidad: "))

Xi = list(map(int, input('Xi: ').split())) 

Fj = list(map(int, input('Fj: ').split())) 

XiFj = []
for i in range(1,N+1):
    XiFj.append(Xi[i]*Fj[i])

total = 0
for i in range(1,N+1):
    total += XiFj[i]

print(total/N)
