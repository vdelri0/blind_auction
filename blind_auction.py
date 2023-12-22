import os
from art import logo

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_highest_bidder(bid_list):
    highest_bidder = {"name": "", "bid": 0}
    for item in bid_list:
        if item["bid"] > highest_bidder["bid"]:
            highest_bidder = item
    print(f"The winner is {highest_bidder['name']} with a bid of ${highest_bidder['bid']}.")

bid_list = []
auction = True

print(logo)
print("Welcome to the secret auction program.")

while auction:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_list.append({"name": name, "bid": bid})
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if bidders == "no":
        auction = False
        calculate_highest_bidder(bid_list)
    elif bidders == "yes":
        cls()
