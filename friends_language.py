#Ê²Ã´Çé¿ö

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'emiya' : 'python',
    }

friends = ['phil', 'sarah', 'lili']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi, " + name.title() + favorite_languages [name].title() + "!")
