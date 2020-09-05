class sample():
    def set_name(self,name):
        self.name=name

    def __add__(self,other):# special fun for operator overloadidng
        full_name=self.name+" "+other.name
        return full_name

first_name=sample()
second_name=sample()
place_name=sample()

first_name.set_name("Anjaly")
second_name.set_name("Krishna")
place_name.set_name("Thodupuzha")

full_name=first_name+place_name # overload + operator
print(full_name)