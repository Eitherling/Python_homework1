def favorite_book(title):
    print("One of my favorite books is " + title.title() +'.')

favorite_book('Alice in wonders')

print('*' * 80)

book = input("\nEnter a name of a favorite book:")
favorite_book(book)
