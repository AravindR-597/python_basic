firstnum=int(input("display multiplication table of "))
secondnum=int(input("enter the range to which multiplication has to be done "))

for  i in range(1,secondnum+1):
    print(firstnum," x ",i," = ",firstnum*i)