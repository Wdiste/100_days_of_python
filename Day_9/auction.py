#### Today's project is a silent auction
#    The program will as for an identifier and bid 
#    then delete the screen so the next person cant see the previous bid
#    save these data in a dictionary

# create the dictionary we will save bids in
# create placeholder for current leader
bidders = {
    "highest_bid" : ["none", 0]
}

def auction():
    name = input("What is your name?")
    current_bid = int(input("How much would you like to bid?"))
    bidders[name] = current_bid

    if current_bid > bidders["highest_bid"][1]:
        bidders["highest_bid"] = [name, current_bid]
    


auction()
print(bidders)



# print("""                         ___________
#                          \\         /
#                           )_______(
#     SILENT                |"""""""|_.-._,.---------.,_.-._
#        AUCTION            |       | | |               | | ''-.
#                           |       |_| |_             _| |_..-'
#                           |_______| '-' `'---------'` '-'
#                           )"""""""(
#                          /_________\\
#                          `'-------'`
#                        .-------------.
#                    jgs/_______________\\""")





# if input("Ready to start? (Y/N)") == "y" or "Y":
#     print("")
# else:
#     print("Goodbye")
