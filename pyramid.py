n = int(input())

for row in range (0,n):
    for col in range(n-row-1):
      print(" ",end="")
    for col in range (2*row +1):
      print("*",end="")
    print()
