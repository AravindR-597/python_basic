class mainclass:
    year = 2020  # class variable work with all object
    # class variable call -- class name.class object


    def __init__(self, name, age, place):  #__init__ is constructor
        self.name = name
        self.age = age
        self.place = place

    # __init__ work as constructor
    def age_adder(self):
        self.age = self.age + 1

    def place_changer(self, place):
        self.place = place

    @classmethod # year is a class variable for defining a function to it
                 # we have to create @classmethod annotation
    def add_year(cls): #cls is attribute
        cls.year=cls.year+1  # call with class name

    def display(self):
        print("Name : " + self.name)
        print("Age : " + str(self.age))
        print("Place : " + self.place)
        print("Year : " + str(mainclass.year))

    @staticmethod # this is for static method for calling something without
                    # affecting the whole clsss
    def display_static():
        print("this is a static call")


mainclass.display_static()


print('\n')
x = mainclass("Aravind", 23, "tdpa")
y = mainclass("anjaly", 21, "thodupuzha")
x.display()
y.display()

print("\n")
#mainclass.year=mainclass.year+1
x.age_adder()
y.age_adder()
x.place_changer("thodupuzha")
y.place_changer("tdpa")
mainclass.add_year()
x.display()
y.display()


