favorite_num = {}

favorite_num['bob'] = [1, 3, 5, 7, 9]
favorite_num['jack'] = [2, 4, 6, 8, 10]
favorite_num['nagi'] = [2, 3, 5, 7, 11]
favorite_num['negisi'] = [4, 8, 12, 16, 20]
favorite_num['charlie'] = [5, 10, 15, 20, 25]

for person, nums in favorite_num.items():
    print(person.title() + ": ")
    for num in nums:
        print(str(num))

    print("\n")
    
