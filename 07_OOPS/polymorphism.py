# Note method overidding is not possible in python

# class add:
#     def sum(self , a , b):
#         return a + b;
#     def sum(self , a , b , c):
#         return a + b + c
    
# obj = add();
# print(obj.sum(3 , 4))

class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def fullname(self):
        print("Car Name is = " , self.model , " , Brand Name is = " , self.brand)

    @staticmethod
    def gen_des():    # for static do not need self
        print("Hello")



class Electic_car(Car):
    def __init__(self , model , brand , Battery):
        super().__init__(brand ,model)
        self.battery = Battery

    def fullname(self):
        print("I am child")

obj1 = Car("BMW" , "M3")
obj2  = Electic_car("Mode 3" , "Tesla" , "200wt")

obj1.fullname()
obj2.fullname()

print(Car.gen_des())