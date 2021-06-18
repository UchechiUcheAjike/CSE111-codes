# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    print()
    gender = input("What is your gender? (M or F): ")
    birthdate = input("What is your birthday?(YYYY-MM-DD): ")
    height_feet = float(input("What is your height (just feet): "))
    height = float(input("What is your height (just inches): "))
    lb_or_stone = input("Are you entering weight in lbs or stones?: " )
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    height = (height_feet * 12) + height

    age = compute_age(birthdate)
    if lb_or_stone == ("stone"):
      weight = float(input("What is your weight?(in stones): "))
      kg_lb = kg_from_stone(weight)
    else:
      weight = float(input("What is your weight?(in pounds): "))
      kg_lb = kg_from_lb(weight)

      

    cm_in = cm_from_in(height)
    bmi = body_mass_index(kg_lb, cm_in)
    bmr = basal_metabolic_rate(gender, kg_lb, cm_in, age)
    
    if bmr >= 3000:
      print("You must be growing!")
    elif bmr < 3000 < 2500:
      print("You seem to be quite average")
    elif bmr < 2500:
      print("You should make sure you are eating enough")


  

    # Print the results for the user to see.
    cm_in /= 100
    print(age)
    print(f"{kg_lb:.2f}")
    print(f"{cm_in:.1f}")
    print(f"{bmi:.1f}")
    print(f"{bmr:.0f}")
    pass


def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years

def kg_from_lb(lb):
   kg = lb * 0.45359237
   return kg
    
def kg_from_stone(stone):
  kg = stone * 6.35029
  return kg


def cm_from_in(inch):
    cm = inch * 2.54
    return cm
    


def body_mass_index(weight, height):
    bmi = (10000 * weight) / (height ** 2)
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    if gender == ("M"):
      bmr = 88.362 + 13.397 * weight + 4.779 * height - 5.677 * age
    elif gender == ("F"):
      bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return bmr
   
    

# Call the main function so that
# this program will start executing.
main()