# -*- coding:utf-8 -*- 

alien_0 = {}
alien_0 ['x_position'] = 0
alien_0 ['y_position'] = 25
alien_0 ['speed'] = 'medium'

print("Original x-position: " + str(alien_0 ['x_position']))

#�ı������˵��ٶȣ���ɿ���
print("Changing alien speed to fast...")
alien_0 ['speed'] = 'fast'

#�����ƶ�������
#���������˵�ǰ�ٶȣ��������ƶ���Զ
if alien_0 ['speed'] == 'slow':
    x_increasement = 1
elif alien_0 ['speed'] == 'medium':
    x_increasement = 2
else:
    x_increasement = 3

#��λ�õ�����λ�ü���λ������
alien_0 ['x_position'] = alien_0 ['x_position'] + x_increasement
print("New x-position: " + str(alien_0 ['x_position']))
