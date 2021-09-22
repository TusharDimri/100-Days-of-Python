import random
import my_module

print(my_module.pi)

print(random.random()) # Generates a random floating point number netween 0.0 and 1.0(1.0 excluded)

print(random.randint(1, 10)) # Both 1 and 10 arr inclusive

l = ["Les Paul", "Stratocaster", "Telecaster", "Acoustic"]
print(random.choice(l))

# Generating random numbers between 0.0 to x(excluding x):-
# x * random.random()
# For e.g. :-
print(random.random() * 5)
