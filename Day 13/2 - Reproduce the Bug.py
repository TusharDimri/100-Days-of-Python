# Next step in debugging is to reproduce the bug that you've encountered. This is because when you encounter it once but you don't encounter it the next time, that becomes a really difficult big to fix.

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# As we can see from the output of above code, we get this error occasionally and this makes the code even harder to debug as the code sometimes works but sometimes it does'nt and sometimes we don't even know that we have a bug or not.

# To solve such problems we have to reproduce the error and fix our code based on this knowledge.

# print(dice_imgs[1]) Fine 
# print(dice_imgs[2]) Fine 
# print(dice_imgs[3]) Fine
# print(dice_imgs[4]) Fine
# print(dice_imgs[5]) Fine
# print(dice_imgs[6]) This line gives an error.  

# Solution for this problem:-

dice_num = randint(0, 5)
print(dice_imgs[dice_num])