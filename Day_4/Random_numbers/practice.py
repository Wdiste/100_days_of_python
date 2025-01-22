import random
import my_module

# random_integer = random.randint(1, 10)
# random_number_0_to_1 = random.random()
# random_uniform = random.uniform(1, 10)

# print(random_integer)
# print(my_module.my_favorite_number)
# print(random_number_0_to_1)
# print(random_uniform)

coin_toss = random.randint(1, 2)

if coin_toss == 1:
    print("Heads")
else :
    print("Tails")