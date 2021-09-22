import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer = [rock, paper, scissors]
print(f"{rock}\n{paper}\n{scissors}")
ch = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
comp = random.randint(0, 2)

if ch == 0:
    if comp == 0:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nIt's a Draw")
    elif comp == 1:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Lose")
    else:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Win")
            
elif ch == 1:
    if comp == 0:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Win")
    elif comp == 1:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nIt's a Draw")
    else:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Lose")
    
elif ch == 2:
    if comp == 0:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Lose")
    elif comp == 1:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nYou Win")
    else:
        print(f"{computer[ch]}\nComputer Choose:\n{computer[comp]}\nIt's a Draw")
