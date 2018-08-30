# -*- coding:utf-8 -*- 

alien_0 = {}
alien_0 ['x_position'] = 0
alien_0 ['y_position'] = 25
alien_0 ['speed'] = 'medium'

print("Original x-position: " + str(alien_0 ['x_position']))

#改变外星人的速度，变成快速
print("Changing alien speed to fast...")
alien_0 ['speed'] = 'fast'

#向右移动外星人
#根据外星人当前速度，决定他移动多远
if alien_0 ['speed'] == 'slow':
    x_increasement = 1
elif alien_0 ['speed'] == 'medium':
    x_increasement = 2
else:
    x_increasement = 3

#新位置等于老位置加上位置增量
alien_0 ['x_position'] = alien_0 ['x_position'] + x_increasement
print("New x-position: " + str(alien_0 ['x_position']))
