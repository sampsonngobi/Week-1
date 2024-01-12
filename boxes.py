# A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. 
# Write a Python program named boxes.py that asks the user for two integers:

# the number of manufactured items
# the number of items that the user will pack per box
# Your program must compute and print the number of boxes necessary t
# o hold the items. This must be a whole number. Note that the last box may
# be packed with fewer items than the other boxes.

#import the math library
import math

#Ask user for the number of items manufactured and the number of items to be packed in a box.
#convert the strings return from the input funtion to integer using the int function
number_of_items = int(input("Enter the number of Items: "))
items_boxes = int(input("Enter the number of items per box: "))

#
number_of_boxes = number_of_items / items_boxes

print()
print(f"For {number_of_items} items, packing {items_boxes} items in each box, you will need {math.ceil(number_of_boxes)} boxes")

