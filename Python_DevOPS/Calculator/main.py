import art
import operator
from replit import clear
print(art.logo)

opr = {
 "+": operator.add,
 "-": operator.sub,
 "*": operator.mul, 
 "/": operator.truediv
}

ind = True
number1 = float(input("What is the  first number? "))
result = number1
for sym in opr:
    print(sym)
while ind:
  operation = input("Pick an operation:  ") 
  number2 = float(input("What's the next number? "))
  
  result = opr[operation](result, number2)
  print(result)
  con = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if con == "n":
    clear()
    ind = False
    break
  



