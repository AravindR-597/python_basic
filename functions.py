def fun(name):
    print("what's up " + name)


nam = "man"
fun(nam)


# arbitory element

def hello(*bat):
    print("elements are " + bat[0], " , " + bat[1], " , " + bat[2])


hello("mercury", "lithium", 'h2so4')


#global and local variable

value=10    #global var

def sample():
    value=30  #local var
    print(value)

sample()
print(value)

#keyword argument

def sample(name,age):  #don't want to check  order  value can be passed by useing keyword  eg:name,age
    print(name,age)

sample(age=10,name="aravind")

#defult argument

def default(name,age=25):
    print(name,age)   # set a default value and print it if we dosent give a value

default(name="aravind")
default(name="aravind",age=30)

# return value

def add(num1,num2):
    sum=num1+num2
    return sum


result=add(2,3)
print(result)