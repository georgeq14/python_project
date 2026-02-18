import random

#create two empty lists
my_numbers = []
winning_numbers = []

#add numbers to the lists
for i in range(0,5):
    my_numbers.append(random.randint(1,69))

for i in range(0,5):
    winning_numbers.append(random.randint(1,69))

#add one more number to the list from 1 to 26
my_numbers.append(random.randint(1,26))
winning_numbers.append(random.randint(1,26))

print(my_numbers)
print(winning_numbers)