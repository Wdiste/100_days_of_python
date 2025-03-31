#### Today's project is a silent auction
#    The program will as for an identifier and bid 
#    then delete the screen so the next person cant see the previous bid
#    save these data in a dictionary

# create the dictionary we will save bids in
# create placeholder for current leader
bidders = {
    "highest_bid" : ["none", 0]
}

def auction(more_bids):
    while more_bids == True:
        name = input("What is your name?  ")
        current_bid = int(input("How much would you like to bid?  ")) # forcing an int because input is interpreted as str
        bidders[name] = current_bid

        if current_bid > bidders["highest_bid"][1]:
            bidders["highest_bid"] = [name, current_bid]
        
        if input("Would you like to make another bid? (Y/N)  ").lower() == "n":
            more_bids = False

    print(f"Congratulations {bidders['highest_bid'][0]}, you are the winner!")
    print(f"{bidders['highest_bid'][0]}, please pay your bill of ${bidders['highest_bid'][1]} at our kiosk.")


print("""                         ___________
                         \\         /
                          )_______(
    SILENT                |"""""""|_.-._,.---------.,_.-._
       AUCTION            |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                   jgs/_______________\\""")
if input("Ready to start? (Y/N)  ").lower() == "y":
    print("Lets meet our first bidder!")
    auction(more_bids = True)
else:
    print("Goodbye")









