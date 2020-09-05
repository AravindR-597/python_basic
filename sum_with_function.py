

#fun with argument and return type

def add(num1,num2):
    sum=num1+num2
    return sum


result=add(2,3)
print(result)

#fun with argument and without return type

def add2(num3,num4):
    sum=num3+num4
    print(sum)

add2(3,4)

#fun without argument and return type

def add3():
    num1=int(input("num1"))
    num2=int(input("num2"))
    print(num1+num2)

add3()

# FUN without argument but with return type

def add4():
    num1=int(input("num1"))
    num2=int(input("num2"))
    sum=(num1+num2)
    return sum

sum=add4()
print(sum)