# -*- coding:utf-8 -*-

# �����ʾ��ֵ�
responses = {}

# ���ñ�־������֧�������Ƿ����
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # ���ʾ������ֵ���
    responses [name] = response
    
    # ѯ���������Ƿ��������
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat.lower() == 'no' or repeat.lower() == 'n':
        polling_active = False

print("\n--- Poll results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
