import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)

flag = True
while flag:
    word = input("Enter a word: ")
    try:
        result = [data_dict[letter.upper()] for letter in word]
        flag = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(result)