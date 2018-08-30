# -*- coding:utf-8 -*-

class Car():
    # 一次模拟汽车的简单尝试
    
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
class ElectricCar(Car):
    # 电动车的独特之处
    
    def __init__(self, make, model, year):
        # 初始化父类的属性
        super().__init__(make, model, year)
        # 初始化电动车的特殊属性
        self.battery_size = 70
    def describe_battery(self):
        # 打印描述电瓶容量的信息
        print("This car has a " + str(self.battery_size) + "-hWh battery.")
        
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
