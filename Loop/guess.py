guess = 0
tries = 0

while guess != 6:
    guess = int(input("Guess the numebr: "))
    tries =   tries + 1
    
print("You have guessed it right after ",tries, "tries!")