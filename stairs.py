
n = 6

for row in range (0 , n):
    for col in range (n - row - 1):
        print("",end="")
    for col in range (row + 1):
        print("*",end="")
    print()
