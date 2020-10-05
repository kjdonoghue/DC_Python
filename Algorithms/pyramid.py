#Pyramid

rows = 9

def build_pyramid(rows):
  spaces = rows -1
  stars = 1
  while rows > 0:
    for i in range(0, spaces):
      print(" ", end="") 
    for i in range(0, stars):
      print('*', end="")
    print()  
    stars += 2
    rows -= 1
    spaces -= 1

build_pyramid(rows) 
    
