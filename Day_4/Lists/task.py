# Lists (Arrays) are a data structure which groups similar data together

# An example of uses is keeping the order of a queue, saving positions based on time of arrival

USA = ["New Jersey", "New York", "The other ones"]

print("\nWhich state has the best pizza?")
print("\n" + USA[0])

# Obvious reminder, Lists(Arrays) start with 0!!!!
# Use negative indeces to access the back of the list

print("\nUse negative indeces to access the back of the list")  
print(USA[-1])

# Command to push to List(Array):
# my_list.append(my_data)

print("Let's add more states!")
USA.append("Delaware")
USA.append("Wisconson")
USA.append("Skibbity Ohio")
print("\n\nLet's see our new list!")
print(USA)

# You can also use .extend() to combine Lists(Arrays)

USA.extend(["Alabama", "Hawaii", "Alaska", "Connecticut"])
print(USA)