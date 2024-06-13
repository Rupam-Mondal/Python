class Car:
    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        print("Car Name is = " , self.model , " , Brand Name is = " , self.brand)

    def get_brand(self):
        return self.__brand
    

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())