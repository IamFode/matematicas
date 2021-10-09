import math

x_deg = float(input())

while x_deg<0 and x_deg>360:
    x = float(input())

x = math.radians(x_deg)

sen = 0

for n in range(50):
    sen += math.pow(-1,n) * (math.pow(x,2*n+1)/math.factorial(2*n+1))

print(round(sen,2))

