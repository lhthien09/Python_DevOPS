#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import logo
actual = random.randint(1,100)

print(logo.logo)
print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose a difficulty. Type 'ease' or 'hard':  ")

if dif == 'hard':
   turns = 5
else:
   turns = 10
print(f"You have {turns} attempts remaining to guess this number.")



while turns >0:
  turns -= 1
  guess = int(input("Make a guess:  "))
  if guess == actual:
    print(f"Exactly!! I am thinking of {guess}")
    break
  if guess > actual:
    print("Too high. \nGuess again.")
  elif guess < actual:
    print("Too low. \nGuess again.")
  print(f"You have {turns} attempts remained.")

if turns == 0: 
  print(f"You've run out of guesses, you lose.")
