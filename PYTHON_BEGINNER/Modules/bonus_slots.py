import random

def play():
    
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
    
   
play()    
while 1:
    print("\n")
    answer = input("Would you still like to play? (y/n): ")
    if answer == "y":
        play()
    elif answer == "n":
        break
    else:
        print("Please enter y or n")
    
    