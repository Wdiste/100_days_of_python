##  we will be making a number guessing game today
##  our lesson is going to look at scope

## use <global> to access variables outside scope of function
import random

computer_guess = random.randint(1, 100)

def guessing_game():
    print("Welcome to my guessing game.  I'm thinking of a number between 1 and 100")
    difficulty = input("\n\nChoose a difficulty: Easy | Medium | Hard:  ")

    if difficulty.lower() == "easy":
        difficulty = 11
    elif difficulty.lower() == "medium":
        difficulty = 6
    elif difficulty.lower() == "hard":
        difficulty = 4


    for guess in range(1, difficulty):
        my_guess = int(input("\nGuess a number: "))
        if my_guess == computer_guess:
            print("\n\nCongrats you guessed right!")
            return 0
        elif my_guess > computer_guess:
            print("Try lower!")
        else:
            print("Try higher!")
    print(f"\n\nThe computer guessed {computer_guess}! Better luck next time!")
    return 0

guessing_game()