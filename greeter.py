# -*- coding:utf-8 -*- 

def greet_user(username):
    #显示简单的问候语
    if username == '':
        print('Hello!')
    else:
        print("Hello, " + username.title() + "!" )

greet_user('')
greet_user('jesse')
