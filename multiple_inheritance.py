class First:
    #def display_first(self): # multi level inheritance
    def display(self):
        print("First")

class Second():
#class Second(First): # multi level inheritance
     #def display_second(self): # multi level inheritance
    def display(self):
        print("Second")

class Third(Second,First):
#class Third(Second): # multi level inheritance
    #def display_third(self):
    def display(self):
        print("Third")

x=Third()
#x.dispaly_first()
#x.display_second()

#x.display_third()

#x.display_first() #multi level inheritance

# this x.display will print second because we have called like
# class Third(second,First)
# if we reverse it then it will print first
# left right rule
# if checks for display fun from left to right
# ie; here from third--second--first
#if it doesn't find display fun in class third it will movet to class second if it doesnt find display there it moves to class first
x.display()

# to find the order of movement from class
print(Third.mro())
# it will print the order


