# -*- coding:utf-8 -*- 

class Car():
    
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
        
    def upgrade_odometer(self, mileage):
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
      # 这里的疑问是--如何使得miles为负数的时候，做出同样不能回滚里程表的提示？
        if miles >= 0:
            self.odometer_reading += miles
        elif miles < 0:
            print("You can't increase a minus odomile.")
