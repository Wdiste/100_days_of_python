### Functions with outputs

### today we're making a calculator

def calculator():
    ### do this
    print("""     __________
    | ________ |
    ||12345678||
    |\"\"\"\"\"\"\"\"\"\"|
    |[M|#|C][-]|
    |[7|8|9][+]|
    |[4|5|6][x]|
    |[1|2|3][%]|
    |[.|O|:][=]|
    \"----------\"  hjw""")

##  put these functions into a dictionary so we can just use "+" "-" etc
##  do not include the parentheses
    def add(a1, a2):
        return a1 + a2
    def subtract(s1, s2):
        return s1 - s2
    def multiply(m1, m2):
        return m1 * m2
    def divide(d1, d2):
        return d1 / d2
    
    operators = {"+" : add,
                 "-" : subtract,
                 "*" : multiply,
                 "/" : divide}
    done = False
    answer = "none"
    while done == False:
        if answer == "none":
            n1 = float(input("What is the first number?  "))
        else:
            n1 = answer
            print(f"\n\nAnswer: {n1} ")

        operation = input("Operation? + - * /  ")
        n2 = float(input("What is the second number? "))

        # using the dictionary prevents us from having to write nested for loops
        answer = operators[operation](n1, n2)
        print(answer)
        

        if input("Would you like to continue? Y/N: ").lower() == "n":
            print("\n\nGoodbye")
            done = True

        


    ### you can call a function by its variable
    ### print(operators["*"](4, 8))
        
calculator()