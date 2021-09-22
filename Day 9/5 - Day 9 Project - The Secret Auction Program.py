from art import logo
import os
from time import sleep

def clear_screen():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

    # As I am in Windows right now:-
    # _ = os.system('cls')
    

print(logo)
print("Welcome to the secret auction orogram.")

there_are_bidders = True
bidders = {}

while there_are_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    ch = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if ch == 'yes':
        sleep(1)
        clear_screen()
        continue
    elif ch == 'no':
        there_are_bidders = False
    else:
        print("Invalid Input")
        continue

Keymax = max(bidders, key= lambda x: bidders[x])
print(f"The winner is {Keymax} with a bid of ${bidders[Keymax]}")