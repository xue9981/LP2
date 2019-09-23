num = [i for i in range(1, 10)]

for i in num:
    if i == 1:
        suffix = 'st'
    elif i == 2:
        suffix = 'nd'
    elif i == 3:
        suffix = 'rd'
    else:
        suffix = 'th'

    print(str(i) + suffix)

    
