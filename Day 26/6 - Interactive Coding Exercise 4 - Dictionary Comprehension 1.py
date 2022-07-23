#  Instructions

"""
You are going to use Dictionary Comprehension to create a dictionary called `result` that takes each word in the given sentence and calculates the number of letters in each word.

Try Googling to find out how to convert a sentence into a list of words.
"""

# **Do NOT** Create a dictionary directly. Try to use **Dictionary Comprehension** instead of a **Loop**.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split(" ")
print(sentence_list)
sentence_dict = {word: len(word) for word in sentence_list}
print(sentence_dict)