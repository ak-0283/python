# recursive function of backward counting

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)

# show(5)


# recursive function of the factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(5))