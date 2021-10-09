N,K = map(int,input().split())

while (N<1 and N>100) or (K<1 and N>100):
    N,K = map(int,input().split())

sum = 0
for i in range(0,N):
    sum += (i+K)/(2+i+K)

print(int(sum)+1)
    




