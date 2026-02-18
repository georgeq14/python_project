bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

#variables
total = 0
my_share = 0

for i in range(len(bill)):
    total = total + bill[i]

"""
Another example of how it can be done 
for item in list:
  total = total + item
"""

my_share = total/4

#print
print(my_share)

