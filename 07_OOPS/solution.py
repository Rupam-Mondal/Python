class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def fullname(self):
        print("Car Name is = " , self.model , " , Brand Name is = " , self.brand)

class Electic_car(Car):
    def __init__(self , model , brand , Battery):
        super().__init__(brand ,model)
        self.battery = Battery


my_car= Car("BMW" , "M3")
print(my_car.brand)
print(my_car.model)
tesla = Electic_car("Mode 3" , "Tesla" , "200wt")
tesla.fullname()
my_car.fullname()