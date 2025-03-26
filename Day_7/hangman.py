import random

####### Today's lesson is one project.  We are building a 'Hangman' game #######

hangman = [
r"""
____
|/   | _   _   ___   _   _ _____ ___  ___  ___   _   _  
|     | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
|     | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| | 
|     |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
|     | | | || | | || |\  | |_\ \| |  | || | | || |\  | 
|     \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/
|_____
""",
""" 
____
|/   |
|   
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|/
|    |
|    
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \\|/
|    |
|   / 
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \\
|
|_____
""",
"""
 ____
|/   |
|   (_)
|   /|\\
|    |
|   | |
|
|_____
"""]

word_bank = [
    "gas",
    "provoke",
    "prediction",
    "slam",
    "addition",
    "coma",
    "sanctuary",
    "self",
    "catch",
    "path",
    "page",
    "theory",
    "incapable",
    "asset",
    "bitter",
    "negative",
    "debt",
    "giant",
    "disclose",
    "hurl",
    "shiver",
    "available",
    "district",
    "warning",
    "accept",
    "therapist",
    "bubble",
    "mass",
    "direct",
    "place"
    ]

## this is initial setup, runs once
counter = 0
print(hangman[counter])

counter += 1

word = word_bank[random.randint(0,19)]
print("let\'s get started! Guess the word before you hang!")

spaces = []
for letter in word:
    spaces.append(" _ ")



## this will be the game loop

while counter < 7:
    if all(word[i] == spaces[i] for i in range(len(word))):
        print(hangman[counter])
        print("        ", *spaces)
        print("Congrats, you won!")
        break

    print(hangman[counter])
    print("        ", *spaces, word)

    positions = []
    char = input("Guess a letter: ")
    if char in word:
        for index, letter in enumerate(word): # enumerate runs through the sequence keeping track of index
            if letter == char:
                positions.append(index)
        for p in positions:
            spaces[p] = char
    else:
        counter += 1

if counter > 6:
    print(hangman[counter])
    print("        ", *spaces, word)
    print("Sorry, you lose!")
