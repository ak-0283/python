# conditional statement

# if elif else statement

# 1st example
# a = int(input("enter you age: "))
# if(a>=18) :
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


# 2nd example
# a = str(input("enter the traffic signal light: "))
# if(a=="red"):
#     print("STOP")
# elif(a=="yellow"):
#     print("look")
# elif(a=="green"):
#     print("GO")
# else:
#     print("you have entered wrong value")

# print("end of code")



# 3rd conditional statement in nesting form
a = int(input("enter your age: "))
if(a>=18):
    if(a>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("you have entered the wrong value")

print("End of code")