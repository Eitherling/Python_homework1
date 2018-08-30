# -*- coding:utf-8 -*-
# 求解一元一次方程
 
print("This program is for equation Ax + B = C.")
 
print("Please input number A.")
numberA = input()
 
print("Please input number B.")
numberB = input()
 
print("Please input number C.")
numberC = input()
 
print("The equation is: " + str(numberA) + ' * x + ' + str(numberB) + ' = ' + \
str(numberC) + ' .')
 
if float(numberA) == 0 and float(numberC) - float(numberB) == 0:
    print('X can be any number.')

elif float(numberA) == 0 and float(numberC) - float(numberB) !=0:
    print('The equation has no solution.')

elif numberA != 0:
    solutionx = (float(numberC) - float(numberB)) / float(numberA)
    print("The equation's solution is x = " + str(solutionx))
