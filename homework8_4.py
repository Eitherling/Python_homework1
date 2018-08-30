def make_shirt(size, sentence = 'I love Python!'):
    print('\nThe size of the shirt is : ' + size.title() +'.' )
    print('\nIt prints: ' + sentence.title())

make_shirt('Large')
make_shirt('middle')
make_shirt('Small', 'It depends!')
