# Unlimited Arguments: 

def add(*args):
    print(args)  # Tuple
    sum = 0
    for n in args:
        sum+=n
    print(sum)

add(1, 6, 7, 3, 8, 10)