from art import logo
import random
from os import system
from time import sleep

def guess_the_number(attempts):
    while attempts > 0:
        if attempts == 1:
            print(f"You have {attempts} attempt remaining.")    
        else:
            print(f"You have {attempts} attempts remaining.")    
            
        guess = int(input("Make a guess: "))

        if guess < guess_num:
            print("Too Low.")
            if attempts > 1:
                print("Guess Again.")
            attempts -= 1

        elif guess > guess_num:
            print("Too High.")
            if attempts > 1:
                print("Guess Again.")
            attempts -= 1

        elif guess == guess_num:
            print(f"You got it! The answer was {guess_num}.")
            break

    if attempts == 0:
        print(f"You've run out of guesses, you lose. The correct answer was {guess_num}")


wantingToPlay = True
while wantingToPlay:
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    guess_num = random.randint(1, 100)

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choice == 'easy':
        attempts = 10
    elif choice == 'hard':
        attempts = 5
    else:
        print("Invalid Input.")
        sleep(2)
        _ = system('cls')
        continue

    guess_the_number(attempts)

    ch = input("Press 'stop' to stop playing and any other key to continue playing: ").lower()
    
    if ch == 'stop':
        print("Thanks for playing out game.")
        wantingToPlay = False
    else:
        _ = system('cls')
        
        