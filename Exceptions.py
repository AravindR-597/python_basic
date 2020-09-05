div=int(input("enter a number"))
try:
    a=1/div
    print(a)
    print("action compleated")

except ZeroDivisionError:
    print('not defined')

print("program ended")
