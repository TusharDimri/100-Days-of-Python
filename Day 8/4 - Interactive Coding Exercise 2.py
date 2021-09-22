"""
## Prime Numbers

# Instructions

Prime numbers are numbers that can only be cleanly divided by itself and 1. 

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)


**You need to write a function** that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

 
 ![](https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H)

Here are the numbers up to 100, prime numbers are highlighted in yellow:

![](https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw)

#Write your code below this line 👇





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
"""

def prime_checker(number):
    i = 1
    for n in range(1, int(number/2)+1):
        if number % n == 0:
            i += 1
    if i > 1:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
        

n = int(input("Check this number: "))
prime_checker(number=n)