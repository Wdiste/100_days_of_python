#  today we are passing inputs through functions
#  simply place variables in the function call to pass their values to the function
#  in python, the strings need to be preceded by the letter 'f' to become 'f strings'
#  these strings will output the value of the variable in the print()

# ###
# def greet(name):
#     print(f"hello {name}")
#     print(f"how are you {name}")
#     print(f"how is the weather")

# greet("bill")
# ###


#####  you can specify parameter<->argument relationship without regard to order 
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in  {location}?")

greet_with(name="Kata", location="New Jersey")