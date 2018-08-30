def show_magicians(magicians):
    for magician in magicians:
        print('Aye, ' + magician.title() +' arrived.')

def make_great(magicians):
    great_magicians = []
    while magicians:
        great_magician = magicians.pop()
        great_magician = 'the great ' + great_magician 
        great_magicians.append(great_magician)
    # print('Show great:')
    # print(great_magicians)
    # print('Show magicans:')
    # print(magicians)
    for magician in great_magicians:
        magicians.append(magician)

magiciansss = ['bob', 'lili', 'ruru']
make_great(magiciansss)
# print(magiciansss)

print("Now begin the great show:")
show_magicians(magiciansss)

# print(magiciansss)

    
