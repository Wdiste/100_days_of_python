from game_data import game_data_dict, vs, logo
import random

### This game is a quessing game on who has more instagram followers

## points accumulate and rounds progress so long as you are correct

###
    # game_data structure:     {
    #                             'name': 'Instagram',
    #                             'follower_count': 346,
    #                             'description': 'Social media platform',
    #                             'country': 'United States'
    #                           }
###
###
    # game starts
    # two comparisons are chosen
    # player chooses which has higher
    # either score and conitnue or fail and lose
###
def start_game():
    total_correct = 0

    ### Access these data with choice_x("name") => or variants: "follower_count" "description" "country"
    choice_1 = random.choice(game_data_dict)
    choice_2 = random.choice(game_data_dict)

    print(f"choice 1: {choice_1}\nChoice 2: {choice_2}")

    print(f"""  {logo}
                \nLevel {total_correct + 1}

""")

start_game()