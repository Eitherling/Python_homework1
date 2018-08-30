class User():
    
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print("The user's name is " + self.first_name + ' ' + self.last_name + '.')
    
    def greeting_user(self):
        print("Hello, " + self.first_name + ' ' + self.last_name + '!')
    
    
user_a = User("Bob", "Huang")
user_b = User("Reid", "Duke")
user_c = User("Ben", "Stark")

user_a.describe_user()

user_c.greeting_user()
