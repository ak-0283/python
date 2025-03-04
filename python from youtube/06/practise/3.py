# waf to find the factorial of n(n is the parameter)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

factorial(5)