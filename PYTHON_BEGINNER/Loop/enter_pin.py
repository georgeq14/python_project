print("BANK OF CODEX")

pin = int(input("Enter your pin code: "))

while pin != 1234:
    print("You have entered the wrong code!")
    pin = int(input("Enter your pin code: "))
    
if pin == 1234:
    print("PIN accepted!")