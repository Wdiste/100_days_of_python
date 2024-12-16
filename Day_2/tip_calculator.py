print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

final_bill = round((bill / people) * ((tip * .01) + 1), 2)

print(f"\nEach diner must pay ${final_bill:.2f}. \nThank you for using our tip calculator")