# dictionaries in python

# info = {
#     # "key": "value",
#     "name": "John",
#     # "learning": "Python",
#     "subject": ["python", "java", "c++"],   # list
#     "topics": ("dictionaries","set"),  # tuple
#     "age": 25,
#     "isAdult": True,
#     "marks": 94.4,
#     12: "twelve",                               #acceptable
#     "12.99": "twelve point nine nine",          #acceptable
# }

# print(info)
# print(type(info))

# print(info["name"])
# print(info["subject"])
# print(info["topics"])   
# print(info["age"])  
# print(info["isAdult"])
# print(info["marks"])
# print(info[12])
# print(info["12.99"])


# info["name"] = "Abhay"              #overwrite
# info["surname"] = "Kumar"  
# print(info)


# creating null dictionary
# null_dict = {}



# nested dictionary
student={
    "name":"abhay kumar",
    "subjects":{
        "physics": 96,
        "chemistry": 93,
        "maths": 80
    }
}

# print(student["subjects"]["maths"])
# print(list(student.keys()))               typecase kr diya   
# print(student.keys())                     #returns all keys
# print(len(student))                       to print the length of the dictionary
# print(len(list(student.keys())))          to print the length of the list of dictionary
# print(student.values())                     to print the values of the dictionary
