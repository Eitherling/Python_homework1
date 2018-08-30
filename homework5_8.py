users = ['status','eitherling','emiya','admin','misty']

# ~ users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging again.')
else:
    print('We need find some users.')
