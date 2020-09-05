class base_class:
    def __init__(self):
        print("base construtor")
   # def dispaly(self):
     #   print("Hello")
    def set_name(self,name):
        self.name=name


class sub_class(base_class): # sub class of base class
    def welcome(self):
        print("Welcome")

    def display_name(self):
        print("Name : "+self.name)


x = base_class()
#x.dispaly()

y = sub_class() #y has acess to both classes
#y.dispaly()
y.welcome()
y.set_name("Aravind R") #aravind  passed to name self.name in base class
                        # but as sub class inherit base class  self.name is avilable in subclass also
y.display_name()

base_class() #by calling this class the construtor automatically works