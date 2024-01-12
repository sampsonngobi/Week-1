"""
Assignment
Write a Python program named tire_volume.py that reads from the keyboard the three numbers
for a tire and computes and outputs the volume of space inside that tire.

"""
#imort the math Library
import math

#ask user for the width, aspect ratio and diameter the tire
print()

width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the tire in inches: "))


#compute the volume of the tire using the formular provided in the instructions 
#get pi from the math library
pi = math.pi

volume = pi * width** 2 *aspect_ratio *(width * aspect_ratio + 2540 * diameter) / 10000000000

#display the volume in litres 
print()
print(f"The appropiate volume is {volume:.2f}")