while 1:
    ph = int(input("Please enter a pH level (0-14): "))

    if ph < 0 or ph > 14:
        print("PLease enter a valid pH level")
    
    else: 
        if ph > 7:
            print("Basic")
        elif ph < 7:
            print("Acidic")
        else:
            print("Neutral")