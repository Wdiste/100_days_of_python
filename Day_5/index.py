# For Loops in python work by indentation
# use a variable to automatically work through a list

fruits = ["apple", "pear", "peach", "strawberry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

# Useful methods like sum exist inherently in python

scores = [99, 98, 99, 97, 97, 96, 98, 90, 69, 100]
total_score = sum(scores)

print(total_score)


# challenge: work out the total value of numbers between 1 and 100
total = 0
for number in range(1, 101):
    total += number
print("1 to 100 sum is: ", total)