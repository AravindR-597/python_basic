class base_class:
    def __init__(self):
        print("base construtor")# base class constructor
   # def dispaly(self):
     #   print("Hello")
    def set_name(self,name):
        self.name=name
        print("baseclass setname :" + self.name)


class sub_class(base_class): # sub class of base class

    def __init__(self):# for constructor overriding
        super().__init__()# for calling base constructor along with sub constructor
        print("sub constructor")

    def welcome(self):
        print("Welcome")

    def set_name(self,name): # for fun overriding
        #self.name=name
        super().set_name(name)#for calling base set name fun
        print("subclass setname :"+self.name)

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

#constructor overriding
#-----------------------

base_class() #by calling this class the construtor automatically works

#let's call sub class
sub_class() # here at the time of execution subclass has no constructor
 # so we can see it also have access to the constructor of base class as this is an inheritance

#if sub class also has a constructor let's check
#now let's call subclass
sub_class()
# so here we see that the construtor of subclass overrides the constructor of base class


#function overriding
#-------------------

#let's add set name fuction to sub class also
y.set_name("Anjaly")

#early when we call set name fun set name in base class was called but here sub class also have set name fun and that is been called
# this is function overridding  "the set name fun in subclass overrides the setname fun in the base class

#overriding break using super().
#------------------------------

#now if we want to call base constuctor along with sub constructor
#super keyword is used
sub_class()
#by using super base constuctor is also called

# super for calling set name in base fun
y.set_name("Sreelatha")
# here by using super we call set name fun in base class along with set name fun in sub class