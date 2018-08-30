class Restaurant():
    
    def __init__ (self, name, cooktype):
        self.name = name
        self.cooktype = cooktype
        
    def describe(self):
        print("The name of restaurant is " + self.name + ".")
        print("The cooktype is " + self.cooktype + ".")
        
    def open(self):
        print("New restaurant is now open.")

my_restaurant = Restaurant("xianjian kezhan", 'Chinese')

my_restaurant.open()
my_restaurant.describe()
