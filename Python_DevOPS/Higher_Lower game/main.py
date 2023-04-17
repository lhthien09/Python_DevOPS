import art
from game_data import data
import random 
from replit import clear

is_over = 0 
current_score = 0
count_A = 0
count_B = 0


print(art.logo)
x1 = random.choice(data)

def display(a, b, c):
     return f"{a}, {b}, {c}"

def game_play(x1):
     global data, current_score
     data.remove(x1)
     x2 = random.choice(data)
     count_A = x1["follower_count"]
     count_B = x2["follower_count"]
     if current_score > 0:
        print('''
        ***************************************
        ***************************************
        ***************************************
        ''')
        print(f"\nYou're right. Current score {current_score}.")
     print('Compare A: ")
     print(display(x1["name"], x1["description"], x1["country"]))
     print(art.vs)
     print('Compare B: ')
     print(display(x2["name"], x2["description"], x2["country"]))
     choose = input("Who has more followers? Type 'A' or 'B': ")
     if count_A > count_B:
       answer = "A"
     else: 
       answer = "B"
     if choose == answer:
       current_score +=1
       game_play(x2)
     else: 
       clear()
       print(art.logo)
       print(f"Sorry, that's wrong. Final score: {current_score}")
       return 
      

is_over = game_play(x1)
       

      
