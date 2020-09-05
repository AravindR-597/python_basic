class MyClass:
  #  def hello(self, n):  # SELF IS AN ARGUMENT. CAN BE REPLACED BY ANY WORD
  #      print("Hello " + n)  # n is for passing the name
        # self is only for passing the object (here x)

    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)


x = MyClass()
name = "aravind"
x.hello(name)
x.print_name()

y=MyClass()
name="anjaly"
y.hello(name)
y.print_name()


