favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite_language is " +
      favorite_languages['sarah'].title() +
      ".")

poll_list = ['edward', 'phil', 'nagi', 'senoue']
poll_list.sort()

for name in poll_list:
    if name in favorite_languages.keys():
        print(" Hi " + name.title() + ", thank for you to join the poll.")
    else:
        print(" Hi " + name.title() + ", please join to our poll.")
        

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edwared': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "'s favorite langugaes are:")
    else:
        print("\n" + name.title() + "'s favorite language is: ")
        
    for language in languages:
        print("\t" + language.title())
        
