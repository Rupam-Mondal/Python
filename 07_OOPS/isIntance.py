class Car:
    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model

    def fullname(self):
        print("Car Name is = " , self.model , " , Brand Name is = " , self.brand)

    def get_brand(self):
        return self.__brand


class Electic_car(Car):
    def __init__(self , model , brand , Battery):
        super().__init__(brand ,model)
        self.battery = Battery

tesla = Electic_car("Mode 3" , "Tesla" , "200wt")

print(isinstance(tesla , Car))