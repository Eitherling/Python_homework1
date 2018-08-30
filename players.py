players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('This table is:\n')
print(players)

print('-' * 80)
print(players[0:3])

print('-' * 80)
print(players[1:4])

print('-' * 80)
print(players[:4])

print('-' * 80)
print(players[2:])

print('-' * 80)
print(players[-3:])

print('Here are the first 3 players on my team:')
for player in players[:3]:
	print(player.title())
