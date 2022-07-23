import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(data_dict)

word = input("Enter a word: ")
result = [data_dict[letter.upper()] for letter in word]
print(result)