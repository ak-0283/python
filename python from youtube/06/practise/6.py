# write a recursive function to print all the elements in a list
# hint: use list and index as parameters

def show(lst, index):
    if(index==len(lst)):
        return
    print(lst[index])
    show(lst, index+1)

show([1,2,3,4,5], 0)