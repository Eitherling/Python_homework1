motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = 0
print(motorcycles)

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(1,'Yata')
print(motorcycles)

motorcycles.insert(-1, 'Hebi')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

print('*'*70)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

print('*'*70)
motorcycles = ['honda', 'yamaha', 'suzuki']
lastOwned = motorcycles.pop()
print('The last motorcycle I owned was a ' + lastOwned.title() + '.')

print('*'*70)
firstOwned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + firstOwned.title() + '.')
print(motorcycles)

print('*'*70)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(1,'Yata')
print(motorcycles)

motorcycles.insert(-1, 'Hebi')
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

print("*" * 70)
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

tooExpensive = 'ducati'
motorcycles.remove(tooExpensive)
print(motorcycles)
