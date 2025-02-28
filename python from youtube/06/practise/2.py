# waf to print the elements of a list in a single line.(list is a parameter)

heroes = ["ironman","spiderman","batman","thor","captain america"]

# print(heroes[0],heroes[1],heroes[2],heroes[3],heroes[4])

# or

# print(heroes[0],end=" ")
# print(heroes[1],end=" ")
# print(heroes[2],end=" ")

# or

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)