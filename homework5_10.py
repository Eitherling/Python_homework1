current_users = ["aKari","buziru","cici","doki","elf"]
new_users = ['Buziru','ciCi',"akari",'goodman','kiki']

current_usersName = []
for username in current_users:
        current_usersName.append(username.lower())

print(current_usersName)

for user in new_users:
    if user.lower() in current_usersName:
        print("User name " + user.title() + " has been used, please change a new one.")
        
    else:
        print("User name " + user.title() + " has not been used.")
