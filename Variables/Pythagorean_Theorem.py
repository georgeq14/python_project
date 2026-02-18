#This exercise is going to focus in being able to get input from the user
#We do this by usiing the inout() function

#Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

#Pythagorean Theorem = c = (a**2 + b**2)**(1/2)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b:"))

c = (a**2 + b**2)**(1/2)

print("Th hypotenus is:", c)