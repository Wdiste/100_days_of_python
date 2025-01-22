# A group of friends is out to lunch and want to play a game to see who pays
# Select a random name from the group

import random

friends = ["Sam", "Sally", "Sarah", "Schlomo", "Jocques"]

print(friends[random.randint(0, 4)])

# Python has random funcs like random.choice()

print(random.choice(friends))