# wap to check if a list contains a palindrome of elements
# hint use copy() methods

list1 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == copy_list1):
    print("list1 is palindrome")
else:
    print("list1 is not palindrome")