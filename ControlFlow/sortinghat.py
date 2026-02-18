# Write code below 💖

# decalaring the variables
Gryffindor = 0
Ravenclaw = 0 
Hufflepuff = 0
Slytherin = 0

# ---------------------------
question_one = int(input("Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\nEnter yor choice here: "))

if question_one == 1:
  Gryffindor += 1
  Ravenclaw += 1
  print(Gryffindor)
  print(Ravenclaw)
elif question_one == 2:
  Hufflepuff += 1
  Slytherin += 1
  print(Hufflepuff)
  print(Slytherin)
else:
  print("Please enter a valid choice. ")

# -----------------------------

question_two = int(input("When I'm dead, I want people to remember me as:\n 1)The Good\n 2)The Great\n 3)The Wise\n 4)The Bold\nEnter your choice here: "))

if question_two == 1:
  Hufflepuff += 2
  print(Hufflepuff)
elif question_two == 2:
  Slytherin += 2
  print(Slytherin)
elif question_two == 3:
  Ravenclaw += 2
  print(Ravenclaw)
elif question_two == 4:
  Gryffindor += 2
  print(Gryffindor)
else:
  print("Please enter a valid choice. ")

# ---------------------------

question_three = int(input("Which kind of instrument mnost pleases your ear?\n 1) The violin\n 2)The trumpet\n 3)The piano\n 4)The drum\nEnter your choice here: "))

if question_three == 1:
  Slytherin += 4
  print(Slytherin)
elif question_three == 2:
  Hufflepuff += 4
  print(Hufflepuff)
elif question_three == 3:
  Ravenclaw += 4
  print(Ravenclaw)
elif question_three == 4:
  Gryffindor += 4
  print(Gryffindor)
else:
  print("Please enter a valid choice. ")


print("The score of each house is: ")
print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')
