########################## EJERCICIOS CAPÍTULO 2 ###############################
source("funciones.R")
library(gtools)

####### 2.1 #######

# a) No son mutuamente excluyentes ya que $O\cap M \neq \subset$

# b)
## 1.
180/400
## 2.
150/400
## 3.
30/400
## 4. P(O\M) = P(O intersección M) / P(M)
(60/400) / (180/400)
## 5. P(M\O) = P(M interseccion O) / P(O)
(60/400) / (200/400)

# c) P(V\H) = P(V) 
(50/400) / (220/400)
150/400

# d) P(A\M) = P(A)
(1/20) / (18/40)
18/40

# e)
## 1. P(A union M) = P(A) + P(M) -P(A inters M)
50/400 + 180/400 - 20/400
## 2. P(A union com(M)) = P(A) + P(H) - P(A intes H)
50/400 + 180/400 - 30/400
## 3. conjunto vacio
## 4. P(M\A) = P(M inters A) / P(A)
20/50

####### 2.5 #######
x <- c("h","m")
permutations(n=2,r=3, v=x, repeats.allowed = TRUE)#Permutaciones con repetición
# exactamente dos de los hijos tengan el mismo sexo
6/8
# tener  un varón y dos mujeres
3/8
# tener tres hijos del mismo sexo
2/8

####### 2.7 #######
x <- c("o","t")
per<-permutations(n=2,r=10, v=x, repeats.allowed = TRUE)#Permutaciones con repetición
# probabilidad que salga todas las veces cara
1/1024
1/2^10 # variaciones con repetición 
# el decimoprimero lanzamiento el resultado sea cruz
1/2

####### 2.8 #######
x <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,"def1","def2")
permutations(n=20,r=2, v=x, repeats.allowed = FALSE)#Permutaciones sin repetición
perm_con_orden(18,2)/perm_con_orden(20,2)

####### 2.9 #######
2/3*2/5 + 1/3*1/2

####### 2.10 #######
x <- c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,"def1","def2", "def3")
permutations(n=20,r=4,v=x,repeats.allowed = FALSE)
#(a)
perm_con_orden(17,4)/perm_con_orden(20,4)
#(b) ??????
perm_n_orden(4,1) * perm_con_orden(17,3) / perm_con_orden(20,4)

####### 2.11 #######
## (b) realizando un esquema de árbol -> La probabilidad que funciones es 0.99
2*(0.9*0.1) + 0.9*0.9

####### 2.12 ####### 
# P(A \cap B \cap C) = 0.95*0.95*0.95
0.95*0.95*0.95
# P(A\cup  B \cup C - (A\cap B) - (B\cap C) - (A\cap C) + (A\cap B \cap C))  = 0.95+0.95+0.95 - 3*(0.95*0.95) 0.95+0.95+0.95 - 3*(0.95*0.95)
0.95+0.95+0.95 - 3*(0.95*0.95) + 0.95*0.95*0.95
# P((A\cup B - A\cap B) \cap C) = 
(0.95 + 0.95 - 0.95*0.95)*0.95
#P((A\cap B)\cup C) = 
(0.95*0.95) + 0.95 - ((0.95*0.95) * 0.95)

####### 2.13 #######
# 0.95n - 0.9025n + 0.95^n = 0.99999 -> n = 3 o 4
0.95 + 0.95 + 0.95 + 0.95 - 5*(0.95*0.95) + 0.95*0.95*0.95*0.95

####### 2.14 #######
#a)
0.25*0.45+0.20*0.55+0.55*0.35
#b)
(0.25*0.45) / (0.25*0.45+0.20*0.55+0.55*0.35)

####### 2.15 #######
# P(D\D) = P(D\C) P(C) / P(D\C) P(C) + P(D\NC)P(CP) 
0.05*0.92 / (.05*0.92 + .3*.08) 





