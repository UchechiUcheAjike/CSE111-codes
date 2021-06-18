def main():
  # Negative 3 5 8 9 10
  # Positive 1 2 4 6 7

  positive_list = []

  negative_list = []

  print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
  print("This program will show you ten statements that you could possibly")
  print("apply to yourself. Please rate how much you agree with each of the")
  print("statements by responding with one of these four letters:")
  print("")
  print("D means you strongly disagree with the statement.")
  print("d means you disagree with the statement.")
  print("a means you agree with the statement.")
  print("A means you strongly agree with the statement.")

  Question1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.\n Enter D, d, a, or A: ")
  
  Question2 = input("2. I feel that I have a number of good qualities.\n Enter D, d, a, or A: ")

  Question3 = input("3. All in all, I am inclined to feel that I am a failure.\n Enter D, d, a, or A: ")

  Question4 = input("4. I am able to do things as well as most other people.\n Enter D, d, a, or A: ")

  Question5 = input("5. I feel I do not have much to be proud of.\n Enter D, d, a, or A: ")

  Question6  = input("6. I take a positive attitude toward myself.\n Enter D, d, a, or A: ")

  Question7 = input("7. On the whole, I am satisfied with myself.\n Enter D, d, a, or A: ")

  Question8 = input("8. I wish I could have more respect for myself.\n Enter D, d, a, or A: ")

  Question9 = input("9. I certainly feel useless at times.\n Enter D, d, a, or A: ")

  Question10 = input("10. At times I think I am no good at all.\n Enter D, d, a, or A: ")

  positive_list.append(Question1)
  positive_list.append(Question2)
  positive_list.append(Question4)
  positive_list.append(Question6)
  positive_list.append(Question7)

  negative_list.append(Question3)
  negative_list.append(Question5)
  negative_list.append(Question8)
  negative_list.append(Question9)
  negative_list.append(Question10)
  total1 = computePositive(positive_list)
  total2 = computeNegative(negative_list)
  finalTotal = total1 + total2
  print(f"your score is {finalTotal}.")
  print("A score below 15 may indicate problematic low self-esteem.")


def computePositive(p_list):
  total = 0
  for item in p_list:
    if item == 'D':
      answer = 0
    elif item == 'd':
      answer = 1
    elif item == 'a':
      answer = 2
    else:
      answer = 3
    total += answer
  return total


def computeNegative(n_list):
  total = 0
  for item in n_list:
    if item == 'D':
      answer = 3
    elif item == 'd':
      answer = 2
    elif item == 'a':
      answer = 1
    else:
      answer = 0
    total += answer
  return total
    


main()