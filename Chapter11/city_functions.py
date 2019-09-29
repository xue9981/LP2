def city_countries(city, country, population=''):
    if population:
        infomation = city.title() + ", " + country.title() + \
        " - population " + str(population)
    else:
        infomation = city.title() + ", " + country.title()

    return infomation

