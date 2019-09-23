def city_country(city, country):
    return city + ", " + country

result = []

while True:
    print("(Enter 'q' for finish)")
    city = input('input city name: ')
    if city == 'q':
        break
    elif city == '':
        print("\n###WARNING###\nPlease input someting for city.\n")
        continue
    country = input('input country name the city beloengs: ')
    if country == 'q':
        break
    elif country == '':
        print("\n###WARNING###\nPlease input somting for country\
. This input will be discard.\n")
        continue
    result.append(city_country(city=city.title(), country=country.title()))

print(result)
       



    
