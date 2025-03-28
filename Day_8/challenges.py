# coding challenge 1: use math to calculate weeks of life remaining if we live to 90

def life_in_weeks(age):
    print(f"You have {(90 - age) * 52} weeks left.")

# life_in_weeks(30)

# coding challenge 2: calculate compatability with a silly name game
# due to limitations on Udemy, no input will be used.  Hard code the inputs

def calculate_love_score(name_1, name_2):
    both_names = name_1 + name_2
    # check how many time 't, r, u, e' occurs in both names
    # check how many times "l, o, v, e" occurs in both names
    true_count = 0
    love_count = 0
    for letter in both_names:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            true_count += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            love_count += 1

    # combine these into a 2 digit number (concatenate)
    print(true_count * 10 + love_count)

    # output the love score

#calculate_love_score("Kanye West", "Kim Kardashian")

