
""""
When you physically exercise to strengthen your heart, you should maintain your heart rate within a 
range for at least 20 minutes. To find that range, subtract your age from 220. This difference is your
 maximum heart rate per minute. Your heart simply will not beat faster than this maximum (220 - age). 
When exercising to strengthen your heart, you should keep your heart rate between
 65% and 85% of your heart's maximum rate.

"""

text = input("Please enter your age: ") #get users age 

age = int(text) #convert the input to an interger 


#compute the max heart rate per minute and the highest and lowest rates 
max_heart_rate = 220 - age 
lowest_rate  = max_heart_rate / 100 * 65
highest_rate = max_heart_rate /100 * 85

print()
print(f"When you physically exercise to strengthen your heart, you should") 
print(f"keep your heart rate between {lowest_rate:.0f} and {highest_rate:.0f}")
print(f"per minute")



