class Restaurant():
    
    def __init__ (self, name, cooktype):
        self.name = name
        self.cooktype = cooktype
        
    def describe(self):
        print("The name of restaurant is " + self.name + ".")
        print("The cooktype is " + self.cooktype + ".")
        
    def open(self):
        print("New restaurant " + self.name + " is now open.")

class IceCreamStand(Restaurant):
    
    def __init__ (self, name, cooktype):
        super().__init__ (name, cooktype)
        
    def offer_flavors(self):
        flavors = ["berry", "cherry", "cookie"]
        print("\nOur flavors are these:")
        for flavor in flavors:
            print(flavor)
            
baihua = IceCreamStand("BaiHua", "Ice tastes.")

baihua.offer_flavors()
