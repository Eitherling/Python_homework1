#什么情况

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    'emiya' : 'python',
    }

print(favorite_languages)

print("Sarah's favorite language is " + favorite_languages['sarah'].title() \
+ '.')

print('-' * 80)

for name in favorite_languages:
    print(name.title())
