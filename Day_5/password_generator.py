import string
import random

symbol_list = []
for c in range(62, 82):
    symbol_list.append(string.printable[c])

print("Welcome to password generator!")
letters = int(input("How many letters would you like?"))
symbols = int(input("How many letters would you like?"))
numbers = int(input("How many letters would you like?"))


# password = ""

# for letter in range(0, letters):
#     password += random.choice(string.ascii_letters)

# for symbol in range(0, symbols):
#     password += random.choice(symbol_list)

# for number in range(0, numbers):
#     password += str(random.randint(0,9))

# print(password)

# hard version

password_list = []
password = ""

for letter in range(0, letters):
    password_list.append(str(random.choice(string.ascii_letters)))

for symbol in range(0, symbols):
    password_list.append(str(random.choice(symbol_list)))

for number in range(0, numbers):
    password_list.append(str(random.randint(0,9)))

random.shuffle(password_list)
for char in password_list:
    password += char
print(password)