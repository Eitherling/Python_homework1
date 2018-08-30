class User():
    
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print("The user's name is " + self.first_name + ' ' + self.last_name \
            + '.')
    
    def greeting_user(self):
        print("Hello, " + self.first_name + ' ' + self.last_name + '!')
    
    
class Privileges():
    def __init__ (self, privileges = ['can add post', 'can delete post', 'can \
ban user']):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)    
class Admin(User):
    
    def __init__ (self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
        
    def show_privileges(self):
        print("\nHi, " + self.first_name + ' ' + self.last_name + ", this is you privileges:")
        user_c.privileges.show_privileges()
user_a = User("Bob", "Huang")
user_b = User("Reid", "Duke")
user_c = Admin("Ben", "Stark")

user_a.describe_user()

user_c.show_privileges()
