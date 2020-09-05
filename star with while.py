# Star pyramid, using while loop
stars = 1
print("This program will make a star pyramid.")
# input
row = int(input("Enter the number of row : "))
# while loop
while row > 0:
    print("  " * row + "" + stars *"  * ")
    stars = stars + 1
    row = row - 1
