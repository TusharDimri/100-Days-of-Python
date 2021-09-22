from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_cards():
    return random.choice(cards)

wantingToPlay = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    


while wantingToPlay == 'y':
    player = []
    computer = []

    for i in range(0, 2):
        player.append(deal_cards)
        player.append(deal_cards)

        computer.append(deal_cards)
        computer.append(deal_cards)
        