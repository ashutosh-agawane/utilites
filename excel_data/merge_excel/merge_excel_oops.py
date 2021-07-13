class Car:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def display(self):
        print("My car model name is {} and buld in year {}".format(
            self.name, self.year))


c1 = Car("Toyota", 25)
c1.display()
