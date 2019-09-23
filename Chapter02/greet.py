friend_names = ['sato', 'watanabe', 'inoue', 'mita', 'nanbu']

greet = "Hello"

while friend_names != []:
    print(greet + ', ' + friend_names.pop().title() + '!')
