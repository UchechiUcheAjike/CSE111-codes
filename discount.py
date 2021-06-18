#Write a Python program named discount.py that takes
#  a customer's subtotal as input. If the subtotal is
#  $50 or greater and today is Tuesday or Wednesday,
#  your program must subtract 10% from the subtotal.
#  Your program must then compute the total amount 
# due by adding sales tax of 6% to the subtotal. Your 
# program must print the discount amount if applicable,
#  the sales tax amount, and the total amount due.

#import datetime module
from datetime import datetime
#subtotal = int(input("Please enter your subtotal: "))
items = ''
done = ''
s = 0
subtotal = 0

while done != 'done':
  items = input('How many items? ')
  s = float(input('How much does it cost? '))
  done = input('Are you done? (Type done if you are): ')
  

  subtotal = subtotal + int(items) * s
  print(f'Your total is {subtotal:.2f}')


current_date_and_time = datetime.now()
weekday = current_date_and_time.isoweekday() -1
print(weekday)
if weekday == 2 or weekday == 3:
  if subtotal >= 50:
    discount = subtotal * .1
    tax = (subtotal - discount) * .06
    total = subtotal - discount + tax 
    print(f"Your discount total is {discount:.2f}")
    print(f"Your total tax is {tax:.2f}")
    print(f"Your grand total is {total:.2f}")
  elif subtotal < 50:
    difference = 50 - subtotal
    ntax = subtotal * .06
    ntotal = subtotal + ntax
    print(f"Your total tax is {ntax:.2f}")
    print(f"Your grand total is {ntotal:.2f}")
    print(f"You are {difference:.2f} dollars away from a 10% discount!")

else: 
    ntax = subtotal * .06
    #btotal = s* .06
    ntotal = subtotal + ntax
    print(f"Your total tax is {ntax:.2f}")
    print(f"Your grand total is {ntotal:.2f}")