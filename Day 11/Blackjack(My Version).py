from art import logo
import random
from os import system, name
import time

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(l):
    if sum(l) == 21 and len(l) == 2:
        return 0

    if sum(l) > 21 and 11 in l:
        l.remove(11)
        l.append(1)        

    return sum(l)
    
def compare(player_score, computer_score):
    if player_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Opponent has a Blackjack"
    elif player_score == 0:
        return "Win with a Blackjack"
    elif player_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif player_score > computer_score:
        return "You Win"
    else:
        return "You Lose"
        

print(logo)        
        

def playGame():
    player = []
    computer = []

    isGameOver = False

    for i in range(0, 2):
        player.append(deal_cards())
        computer.append(deal_cards())

    while not isGameOver:
        user_score = calculate_score(player)
        computer_score = calculate_score(computer)

        print(f"Your cards: {player}, current score = {user_score}") 
        print(f"Computer's first card: {computer[0]}") 

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            isGameOver = True
        else:
            ch = input("Type 'y' to get another card, type 'n' to pass: ")       
            if ch == 'y':
                player.append(deal_cards())
            else:
                isGameOver = True

    while computer_score < 17 and computer_score != 0:
        computer.append(deal_cards())
        computer_score = calculate_score(computer)
        
    print(f"Your final hand: {player}. final score: {user_score}")
    print(f"Computer's final hand: {computer}. final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    time.sleep(1)
    if name == 'nt':
        _ = system('cls')
    else:
        _ - system('clear')
        
    print(logo)
    playGame()
