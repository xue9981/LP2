def make_album(singer_name, album_name, sing_num=''):
    album = {}
    album['singer_name'] = singer_name.title()
    album['album_name'] = album_name

    if sing_num != '':
        album['sing_num'] = sing_num

    return album

result = []
while True:
    print("Enter 'q' for quit")
    singer_name = input("Please input singer's name: ")
    if singer_name == 'q':
        break
    elif singer_name == '':
        print("\n###WARNING###\nPlease input someting for\
 singer name.\n")
        continue

    album_num = input("Please input for songs number in album: ")
    if album_num == 'q':
        break
    elif album_num == '':
        print("\n###WARNING###\nPlease input someting for\
 songs in album.\n")
        continue

    sing_num = input("If you need, please input number of the songs: ")
    if sing_num != '':
        sing_num = sing_num

    result.append(make_album(singer_name, album_num, sing_num))

print(result)
