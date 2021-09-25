# Thre is no such thing as block scope in Python. This means that if we declare a variable inside a block(if-else or loops) then it does not mean that the scope of that variable is limited to that block.

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level == 3:
    new_enemy = enemies[0] # This is a global variable
    print(new_enemy)

print(new_enemy)

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        second_enemy = enemies[1]
        print(second_enemy)

# print(second_enemy) Error

i = 1

while(i > 0 and i <= 10):
    print(i, end=" ")
    i += 1

print(i)