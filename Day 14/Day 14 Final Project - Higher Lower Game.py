import random
import art
import game_data
from os import system

GameNotOver = True
score = 0

def getData():
    articles = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    data = random.choice(game_data.data)

    name = data['name']

    followers = data['follower_count']

    desc = data['description']
    if desc[0] in articles:
        desc = "An " + desc
    else: 
        desc = 'A ' + desc
        
    country = "from " + data['country']

    l = [name, followers, desc, country]

    return l

    

def userIsRight():
    global score
    score += 1
    print(f"You're right! Current Score is {score}")


a = getData()
print(art.logo)


while GameNotOver:
    print(f"Compare A: {a[0]}, {a[2]}, {a[3]}")

    print(art.vs)

    b = getData()

    if a == b:
        continue
    
    print(f"Against B: {b[0]}, {b[2]}, {b[3]}")
        
    choice = input("Who has more followers? A or B: ")

    if choice == 'A' and a[1] > b[1]:
        _ = system('cls')
        print(art.logo)
        userIsRight()
        a = b        
        continue

    elif choice == 'B' and b[1] > a[1]:
        _ = system('cls')
        print(art.logo)
        userIsRight()
        continue

    else:
        GameNotOver = False
        _ = system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")