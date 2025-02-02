# find the greatest of 3 no. entered by user.

a=int(input("Enter a 1st no.: "))
b=int(input("Enter a 2nd no.: "))
c=int(input("Enter a 3rd no.: "))

if(a>b and a>c):
    print("1st no is greater")
elif(b>a and b>c):
    print("2nd no is greater")
elif(c>a and c>b):
    print("3rd no. is greater")
else:
    print("you have entered wrong input")

print("end of code")