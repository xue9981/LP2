def make_car(maker, car_type, **other_info):
    car_info = {}
    car_info['maker'] = maker
    car_info['car_type'] = car_type
    
    for other_key, other_value in other_info.items():
        car_info[other_key] = other_value

    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
