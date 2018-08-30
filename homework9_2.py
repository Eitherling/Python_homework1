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

print('*' * 80)

your_restaurant = Restaurant("longmen mianguan", "Gongfu")
libais_restaurant = Restaurant("xinghua cun",'bar')

print('\nThe new coming restaurant:')
print("My restaurant's name is: " + my_restaurant.name.title() + '.')
print("The style of my restaurant is :" + my_restaurant.cooktype.title() + '.')

print("\nYour restaurant's name is: " + your_restaurant.name.title() + '.')
print("The style of your restaurant is: " + your_restaurant.cooktype.title() + '.')

print("\nLibai's restaurant's name is: " + libais_restaurant.name.title() + '.')
print("The style of Libai's restaurant is: " + libais_restaurant.cooktype.title() + '.')
