magicians = ['eric', 'mei', 'bob', 'alice']
magicians_copy = []

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for magician in magicians:
        magicians[magicians.index(magician)] = "the Great " + magician
    return magicians

magicians_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_copy)

