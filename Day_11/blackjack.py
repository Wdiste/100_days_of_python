#### Capstone project: Blackjack
#
#
#
##   Blackjack is a game where a player tries to get closer to 21 than the dealer

import random


def blackjack():
    deck = { 
        "A" : 11,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "10" : 10,
        "J" : 10,
        "Q" : 10,
        "K" : 10
        }
    player_hand = [0]
    dealer_hand = [0]
    stand = False
    
    #############################################################################
    def hand_value(hand, deck):
        value = 0
        aces = 0

        for card in hand[1:]: ### seen here is an example of LIST SLICING.  1 -> start index
            if card == "A":   #                                             : -> until end with no number(used like range)
                aces += 1     #                                             Syntax -> [start:stop:step]
            value += deck[card]

            while value > 21 and aces:
                value -= 10  # Count one Ace as 1 instead of 11
                aces -= 1
        if value > 21:
            return "Bust"
        elif value == 21:
            return "Blackjack!"
        else:
            return value
    #############################################################################

    if input("Would you like to play blackjack? (Y/N) 🂡 🂮 ").lower() == "y":
        print("Let's Play!\n\n")
        for i in range(2):
            player_hand.append(random.choice(list(deck)))
            dealer_hand.append(random.choice(list(deck)))
            player_hand[0] = hand_value(player_hand, deck)
            dealer_hand[0] = hand_value(dealer_hand, deck)  
    else:
        player_hand[0] = "Goodbye"
        print("Goodbye")
        return
       
    while stand == False and type(player_hand[0]) == int:
        print(f"Dealer: {dealer_hand[1]}, 🂠\nPlayer: {player_hand[1:]} Total: {player_hand[0]}")
        hit_or_stand = input("Would you like another card?").lower()
        if hit_or_stand == "n":
            stand = True
        elif hit_or_stand == "y":
            player_hand.append(random.choice(list(deck)))
            player_hand[0] = hand_value(player_hand, deck)

    print(f"Dealer: {dealer_hand[1:]}\nPlayer: {player_hand[1:]} Total: {player_hand[0]}")

    if player_hand[0] == "Blackjack!":
        print("\n\nCongrats! Player wins!")
    elif player_hand[0] == "Bust":
        print("\n\nDealer wins! Better luck next time!")
    return 0

blackjack()