# -*- coding:utf-8 -*- 

def greet_user(username):
    #��ʾ�򵥵��ʺ���
    if username == '':
        print('Hello!')
    else:
        print("Hello, " + username.title() + "!" )

greet_user('')
greet_user('jesse')
