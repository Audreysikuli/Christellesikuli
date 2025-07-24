## if statements

'''
syntax

if condition
   logic
elif condition
   logic
else:
   logic:
   
'''

## A program that accepts a number from the user (1-9)
# it tells him the number entered

print("welcome to Number Teller!")
number = int (input("please enter a number between 1 and 9"))
if number ==1:
   print("you have entered Numer one")
elif number ==2:
   print("you have entered Numer two")
elif number ==3:
   print("you have entered Numer three")
elif number ==4:
   print("you have entered Numer four")
elif number ==5:
   print("you have entered Numer five")
elif number ==6:
   print("you have entered Numer six")
elif number ==7:
   print("you have entered Numer seven") 
elif number ==8:
   print("you have entered Numer eight")  
elif number ==9:  
   print("you have entered Numer nine")  
else:
   print("Invalid, please enter a number between 1 and 9")  