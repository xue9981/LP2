liver_dic = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'indus': 'india',
    }

for country, liver in liver_dic.items():
    print("The " + liver.title() + " runs throught " +
          country.title())

for country in sorted(liver_dic.keys()):
    print(country.title())

for liver in sorted(liver_dic.values()):
    print(liver.title())
    
