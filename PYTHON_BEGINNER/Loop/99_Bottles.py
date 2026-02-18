# bottles = 99


# while bottles != 0:
#     print(f'{bottles} bottles of beer on the wall\n {bottles} bottles of beer \n Take one down and pass it around')
#     bottles = bottles -1  

for i in range(99, 0, -1):
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print('Take one down, pass it around')
  print(f'{i-1} bottles of beer on the wall')