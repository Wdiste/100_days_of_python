print("Welcome to Python Pizza Deliveries!")

total_price = 0

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

print("\n=============================")
if size == "S" or size == "s":
    total_price += 15
    print("\n Small pizza:         $15.00 ")
    if pepperoni == "Y" or pepperoni == "y":
        total_price += 2
        print("              add pep  $2.00 ")
    if extra_cheese == "Y" or extra_cheese == "y":
        total_price += 1
        print("           extra chse  $1.00 ")
elif size == "M" or size == "m":
    total_price += 20
    print("\n  Med pizza:          $20.00 ")
    if pepperoni == "Y" or pepperoni == "y":
        total_price += 3
        print("              add pep  $3.00 ")
    if extra_cheese == "Y" or extra_cheese == "y":
        total_price += 1
        print("           extra chse  $1.00 ")
elif size == "L" or size == "l":
    total_price += 25
    print("\n  Lrg pizza:          $25.00 ")
    if pepperoni == "Y" or pepperoni == "y":
        total_price += 3
        print("              add pep  $3.00 ")
    if extra_cheese == "Y" or extra_cheese == "y":
        total_price += 1
        print("           extra chse  $1.00 ")

print(f"\n\n  Total price: {total_price}\n\n  Thank you for your custom.")