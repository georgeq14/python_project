while 1:
    print("========================================")
    print("Area Calculator")
    print("========================================")
    
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 3:
        side = int(input("side: "))
        area = side * side
        print("Area of the Square is: ", area)
        
    elif choice == 2:
        length = int(input("length: "))
        width = int(input("width: "))
        area = length * width
        print("Area of the Rectangle is: ", area)
        
    elif choice == 1:
        height = int(input("height: "))
        base = int(input("base: "))
        
        area = (height * base)/2
        
        print("Area of the Triangle is: ", area)
        
    elif choice == 4:
        radius = int(input("radius: "))
        area = 3.14 * radius * radius
        print("The are of the circle is: ", area)
    
    elif choice == 5:
        print("Thank you for using this calculator!")
        break
    
    else:
        print("The number you have entered is not valid.")
        print("PLease try again.")
    

    
