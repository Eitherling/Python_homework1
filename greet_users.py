# -*- coding:utf-8 -*-

def greet_users(names):
    # 对列表中的每个用户进行简单问候
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users (usernames)
