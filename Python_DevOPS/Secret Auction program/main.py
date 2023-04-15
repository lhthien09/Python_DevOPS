from replit import clear
from art import logo
print(logo)

value = 0
dict = {}
while value == 0:
  name = input("What is name input?")
  price = input("What is the Bid price?")
  dict[name] = float(price)
  decision = input("If there are other users who want to bid?  Yes/No  ")
  if decision == "No":
    value = 1
    break
  clear()
# print(dict)

def find_highest_bidder(bidding_records):
  max = float("-inf")
  max_key = ""
  for thing in dict:
    if max < dict[thing]:
      max = dict[thing]
      max_key = thing
  print(f"{max_key} is the winner with the bid of {max}")

find_highest_bidder(dict)


