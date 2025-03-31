# in python, tables are called dictionaries

# syntax looks like:

my_dictionary = {
    "bug" : "Something wrong with your code",
    "Program" : "Blocks of code which perform a task"
}

# values are accessed by their "key"
# it is important that the data type is consistent with the key ( str -> str, int -> int)

print(my_dictionary["bug"])

# to add data, use a key as a variable

my_dictionary["Keyboard"] = "The tool you use to type"

print(my_dictionary)

#  you can declare an empty dictionary or wipe an existing dictionary the same way

new_dictionary = {}
my_dictionary = {}

print(my_dictionary)

# When printed, the dictionary by default returns the keys
# print the key value pair like this:

my_dictionary = {1 : "lemons", 2 : "apples", 3 : "bananas"}

for item in my_dictionary:
    print(item)                 # prints the key
    print(my_dictionary[item])  # prints the value

# NESTING

# you can load dictionaries with other dictionaries and lists

travel_log = {
    "France" : ["Paris", "Lyon", "Normandy"],
    "Germany" : [],
    "Italy" : ["Milan", "Tuscany"]
}

# access inner lists in 2-d manner like:

print(travel_log["France"][1])

# add dictionaries to other dictionaries with the same key - value system
my_dics = {1 : travel_log,
           2 : my_dictionary}

print(my_dics)

# precise data retrieved in multiple dimensional style
# find "Tuscany" in our travel list with this 3-d prompt:

print(my_dics[1]["Italy"][1])