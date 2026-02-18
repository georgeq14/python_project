#import pi from math module
from math import pi 
#import choice from random as ch
from random import choice as ch

#Create the planets list
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

#create a fucntion for getting the area of the planets
def area(r):
    area = 4*pi*(r*r)
    
    print(f'The area of {random_panet} is {area}')

#use ch to get a random planet from the planets list
random_panet = ch(planets)

if random_panet == 'Mercury':
    r = 2440
    area(r)
elif random_panet == 'Venus':
    r = 6052
    area(r)
elif random_panet == 'Earth':
    r = 6371
    area(r)
elif random_panet == 'Mars':
    r = 3390
    area(r)
elif random_panet == 'Saturn':
    r = 58232
    area(r)
else:
    print("oops! an error occured")