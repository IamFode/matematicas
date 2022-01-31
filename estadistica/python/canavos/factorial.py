def factorial(n):
    if n == 0:
        return 1
    else:
        sum = 1
        for i in range(1,n+1):
            sum *= i
        return sum

