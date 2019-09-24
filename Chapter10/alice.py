filename = "alice.txt"

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist"
    print(msg)
else:
    #calculate how many words in this story
    words = contents.split()
    num_words = len(words)
    print("The file " + " has about" + str(num_words) + " words")

    
    
    
