# fibonacci
def fibonacci(n):
    a = -1
    b = 1
    c = 0
    for i in range(1,n+1,1):
        c = a + b
        a = b
        b = c
        return a

# input
x = int(input("Enter a number: "))

# print result
print("Fibonacci number is: ", fibonacci(x))
