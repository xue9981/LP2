user_0 = {
    "username": 'efermi',
    "first": "evrico",
    "last": "fermi",
    }

for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value + "\n")

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite_language is " +
          language.title())

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

        

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")
    
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language)


