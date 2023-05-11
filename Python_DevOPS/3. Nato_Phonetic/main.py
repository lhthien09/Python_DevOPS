# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")



# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
dict = {row.letter: row.code for (ind, row) in df.iterrows()}
print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word:")
letters = [dict[l.upper()] for l in user]
print(letters)

