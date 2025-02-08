# dictionaries in python

info = {
    # "key": "value",
    "name": "John",
    # "learning": "Python",
    "subject": ["python", "java", "c++"],   # list
    "topics": ("dictionaries","set"),  # tuple
    "age": 25,
    "isAdult": True,
    "marks": 94.4,
    12: "twelve",                               #acceptable
    "12.99": "twelve point nine nine",          #acceptable
}

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
null_dict = {}