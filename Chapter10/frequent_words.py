words = ''
key_words = ''
while True:
    print("Enter 'q' to quit")
    words = input("Please input something: ")
    key_words = input("Plese input word you want to count: ")
    if words == 'q' or key_words == 'q':
        break 
    print("Key words " + "'" + key_words + "'" + " appears " + \
          str(words.lower().count(key_words)) + " time/times.\n")

    
    
    
    
