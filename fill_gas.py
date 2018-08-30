class Car():
    def __init__(self,year):
        self.year = year
    
    def fill_gas(self):
        print("Filling the gas now, please wait.")

class ElecCar(Car):
    def __init__(self,year):
        super().__init__(year)
        
    def fill_gas(self):
        print("You can't fill gas in a electric car.")
        
my_tesla = ElecCar('1999')
my_tesla.fill_gas()
