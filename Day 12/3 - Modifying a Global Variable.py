enemies = 1 # Global Scope

def increase_enemies():
    global enemies
    enemies += 1 # Here we are modifying the gloobal variable.
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

