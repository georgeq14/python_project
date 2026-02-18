
#variables
height = int(input("Enter the height of the cyclone: "))
credits = int(input("Enter the number of credits to be spent: "))

#use a combination of relational and logical operators to create their rules

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enought to ride the cyclone!")
elif height >= 137 and credits < 10:
    print("You do not have enough credits to ride the cyclone!")
else:
    print("You are not tall enought and lack in credits to be abel tor ide the cyclone!")
    
    