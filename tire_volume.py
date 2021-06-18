#The size of a car tire in the United States is represented 
# with three numbers like this: 205/60R15. The first number 
# is the width of the tire in millimeters. The second number 
# is the aspect ratio. The third number is the diameter in 
# inches of the wheel that the tire fits. The volume of space
#  inside a tire can be approximated with this formula:




#import the math module so that I can use math.pi.
import math

#print a description of what the program does.
print ('')
print ('This program reads from the keyboard the three numbers for a tire')
print ('and computes and outputs the volume of space inside that tire.')

#Get the user input (width, ratio, diameter).
width  = int(input('Enter the width of the tire in millimeters (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

#compute the volume of space inside a tire.
volume = math.pi * width * width * ratio *(width * ratio + 2540 * diameter) / 10000000

#Round the surface area to one digit after decimal point.
volume = round(volume, 1)

#Print and empty line to acheive the space in the sample
#print the volume of space inside tire for the user to see.
print()
print(f'The approximate volume is {volume} milliliters.')




#Many companies wish to understand the needs and wants of their 
# customers more deeply so the company can create products that 
# fill those needs and wants. One way to understand customers 
# more deeply is to record the values entered by customers while 
# they are using a program and then to analyze those values. One 
# common way to record values is for a program to store them in 
# a file.


#Gets the current date from the computer's clock.
from datetime import datetime
current = datetime.now()
date = current.strftime("%y-%m-%d")

#Input from customer
buy = input ("Do you want to buy tires with the dimensions that you entered? (Yes/No): ")

 
#IF and ELSE statements to determine if the customer wants to make a purchase
if buy == "Yes": 
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    phone_number = input("Please enter your phone number: ")
    farewell_prompt = print("Thank you for your patronage, hope to have you come back soon.:) ")
else:
    print("Thank you for visiting our store, please come back again, cheers. ")

#Opens a text file named volumes.txt for appending.
with open ("volumes.txt", mode= "at") as volumes_file:
    if buy == "Yes":
        print(f"{date}, {width}, {ratio}, {diameter}, {volume: .1f}, {first_name}, {last_name}, {phone_number}", file = volumes_file)
    else:
        print(f"{date}, {width}, {ratio}, {diameter}, {volume: .1f}", file = volumes_file)








