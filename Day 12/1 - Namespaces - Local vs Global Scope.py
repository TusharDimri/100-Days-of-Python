enemies = 1 # Global Scope

def increase_enemies():
    enemies = 2 # Local Scope
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

#  Local Scope : This is linited to a block of code.

player_health = 10

def drink_potion():
    potion_strength = 1
    print(player_health)
    print(potion_strength)

drink_potion()
print(player_health)

# print(potion_strength)
#  Above line gives an error because potion_strength is a local variable and its scope is limited to the function drink_potion()

# This concept of global and local doesn't just apply to variables. It also applies to function and basically anything else we name. This concept is called 'Namespace'.

def func1():
    print("Hello", end=" ")
    def func2():
        print("World")
    func2()

func1()
        