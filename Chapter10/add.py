activate = True
while activate:
    print("Enter 'q' to quit")
    try:
        first = input("input first integer: ")
        second = input("input second integer: ")
        if first == 'q' or second == 'q':
            activate = False
            break
        first = int(first)
        second = int(second)
    #except TypeError:
    except ValueError:
        print("please input integer only!")
    else:
        result = first + second
        print("first add second is: " + str(result))
        
