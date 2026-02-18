# import random

# dice = [1, 2, 3, 4, 5, 6]

# print(random.choices(dice, k=3))

import random

#Create a symbols list
symbols = ['🍒',' 🍇', '🍉', '7️⃣']

#create a results variable that uses the .choices() method from the random module and get three random symbols.
results = random.choices(symbols, k=3)

print(f"{results[0]}  | {results[1]} | {results[2]}")

if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("Jackpot!")
elif results[0] == results[1] == results[2]:
    print("Minor Prize!")
else:
    print("Nice Try!")