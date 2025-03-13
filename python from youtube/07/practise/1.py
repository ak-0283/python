# create a new file "practice.txt" using python.add the following data in it:
# hi everyone,
# we are learning file I/O
# using java
# i like programming in java

# with open("practics.txt","w") as f:
#     f.write("hi everyone \n we are learning file i/o \n using java \n i like programming in java")



# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)



def check_for_word(): 
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")  

check_for_word()