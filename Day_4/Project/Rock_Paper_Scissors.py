import random

print("\nWelcome to Rock Paper Scissors")


user_throw = int(input("\n\nType 0 for Rock, 1 for Paper, or 2 for Scissors"))
computer_throw = random.randint(0, 2)

print(f"user: {user_throw}\ncomputer: {computer_throw}")
results = [[["It's a draw!"], ["Sorry, you lose!"], ["Congrats, you win!"]], 
           [["Congrats, you win!"], ["It's a draw!"], ["Sorry, you lose!"]],
           [["Sorry, you lose!"], ["Congrats, you win!"], ["It's a draw!"]]]

print("User chooses:")
if user_throw == 0:
    print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
elif user_throw == 1:
    print("""
                _______
            ---'    ____)_
                    ______)
                    _______)
                    ______)
            ---.________)
            """)
else:
    print("""
                ______
            ---'   ___)____
                    _______)
                ____________)
                  (____)
            ---.__(___)
            """)
    
print("Computer chooses:")
if computer_throw == 0:
    print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
elif computer_throw == 1:
    print("""
                _______
            ---'    ____)_
                    ______)
                    _______)
                    ______)
            ---.________)
            """)
else:
    print("""
                ______
            ---'   ___)____
                    _______)
                ____________)
                  (____)
            ---.__(___)
            """)

print(*results[user_throw][computer_throw])