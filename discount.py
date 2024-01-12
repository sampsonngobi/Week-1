"""""
Assignment
Work as a team to write a Python program named discount.py 
that gets a customer’s subtotal as input and gets the current
day of the week from your computer’s operating system. Your 
program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer’s
operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. Your program must 
then compute the total amount due by adding sales tax of 6% to the subtotal. 
Your program must print the discount amount if applicable, the sales tax amount, 
and the total amount due.

Core Requirements
Your program asks the user for the subtotal but does not ask the user for the day 
of the week. Your program gets the day of the week from your computer’s operating system.
Your program correctly computes and prints the discount amount if applicable.
Your program correctly computes and prints the sales tax amount and the total amount due.
"""
#import the timedate library
from datetime import datetime

#Ask the customer for a subtotal amount. 
#subtotal_amount = float(input("Please enter a subtotal amount: ")) 

#strech 2
#asks the user for a price and a quantity and computes the subtotal. 
#This loop should repeat until the user enters "0" for the price.

subtotal_amount = 0
price = ""

while price != 0:
    price = float(input("Enter price (enter 0 to quit): "))
    if float(price == 0):
        break
    quantity = float(input("Enter quantity: "))

    subtotal_amount += price * quantity
print(f"Subtal amount: ${subtotal_amount:.2f}")

#Get the current day of the week
current_date= datetime.now()
current_day = current_date.weekday()
    
#Check if the subtotal is $50 or greater and the day of the week is Tuesday or wedsnesday and give a 10% discount.
if subtotal_amount >= 50 and (current_day == 1 or current_day == 3):
    discount = round(subtotal_amount * 0.10, 2)
    print(f"Discount amount: ${discount:.2f}")
    subtotal_amount -= discount

#strectch 1
# if the subtotal is less than 50 and the day is Tuesday or wednesday.
# inform the user the amount to qualify for the day's discount.    
elif subtotal_amount < 50 and (current_day == 1 or current_day == 3):
    difference = round(50 - subtotal_amount, 2)
    print(f"You are ${difference} away from getting the day's discount")

#Add a 6% sales tax to the subtotal 
sales_tax = round(subtotal_amount * 0.06, 2)
print(f"Sales tax amount: ${sales_tax:.2f}")

#compute the total amount due
total_amount_due = subtotal_amount + sales_tax
print(f"Total amount due: ${total_amount_due:.2f}")
    

        




