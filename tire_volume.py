"""

AUTHOR: SAMPSON CHINEDU NGOBI

Assignment
Write a Python program named tire_volume.py that reads from the keyboard the three numbers
for a tire and computes and outputs the volume of space inside that tire.

Exceeding the Requirements
My program will estimate the price of the tire and prints it to the user using a function 
It will aslo ask the user if they want to buy and if the response is yes,
the user is asked for some personal information. 

"""
#imort the Libraries - math and datetime
import math
from datetime import datetime

#ask user for the width, aspect ratio and diameter the tire
print()

width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))


#compute the volume of the tire using the formular provided in the instructions 
#get pi from the math library
pi = math.pi

volume = pi * width** 2 *aspect_ratio *(width * aspect_ratio + 2540 * diameter) / 10000000000

#estimate the price of the tire 
def price_estimation():
    price = 0
    if diameter <= 20:
       price = 50
       print(f"Price is estimated at ${price}") 
    elif diameter >=21:
        price = 100
        print(f"Price is estimated at ${price}") 

#display the volume in litres 
print()
print(f"The appropiate volume is {volume:.2f} liters")
price_estimation()

#confirm buying interest
buy_interest = input("Would you like to purchase a tire(Yes/No): ")
if buy_interest == "yes":
    name = input("Please enter your full name: ")
    contact_info = input("Enter your cell phone number: ")
    
    
else:
    print("Thank you for using our app. Let us know when you would like to buy a tire")

#get the current date 
current_date = datetime.now(tz=None)

#open and appent info to file 
with open("volumes.txt", "at") as volumes_file:
    if buy_interest == "yes":
        print(f"Customer Information: {name}, {contact_info}" , file=volumes_file)    
    print(f"{current_date: %Y-%m-%d}, {round(width)},  {round(aspect_ratio)},  {round(diameter)},  {volume:.2f}", file=volumes_file)
    


