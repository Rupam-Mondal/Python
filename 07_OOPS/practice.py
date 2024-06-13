class Bike:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def print(self):
        print(self.brand)

class ElectricBike(Bike):
    def __init__(self , brand , model , battery):
        super().__init__(brand , model)


mybike = ElectricBike("BMW" , "s1000rr" , "200wt")
mybike.print()