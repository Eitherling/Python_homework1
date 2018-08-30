# -*- coding:utf-8 -*-

# 设置问卷字典
responses = {}

# 设置标志变量，支出调查是否继续
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # 把问卷储存在字典中
    responses [name] = response
    
    # 询问其他人是否继续调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat.lower() == 'no' or repeat.lower() == 'n':
        polling_active = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
