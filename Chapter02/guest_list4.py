from board import board, invite
# guests list
list = ['watanabe', 'turuoka', 'nakatani']

# print invitation
invite(list)

# people to remove from guest list
old_guest = "turuoka"
# people to add in guest list 
new_guest = "sirahige"

# print updated news
message = "Because " + old_guest.title() + " have someting to do on May 5, " + new_guest.title() + " will come on lunch on May 5 in alternitive."

# remove old_guest form list
list.remove(old_guest)
# add new_guest in list
list.append(new_guest)

board(message, list)

# update news
message = "Because I found a larger restaurant, "\
      + "I determined to change the restaurant, and will invite more three guest to the lunch"

# the new guest to invite
new_guest1 = "hasimoto"
new_guest2 = "nagi"
new_guest3 = "senoue"

# add new guest to the list
list.insert(0, new_guest1)
list.insert((list.__len__() // 2), new_guest2)
list.append(new_guest3)

board(message, list)

# update news
message = "So sorry to everyone to join the lunch, but I have a news that the " \
      + "lunch can't come on time. I have no choice but to invite only two "\
      + "guest to have the lunch together."

board(message, list)

# print sorry statement to the friend you can't invite
while list.__len__() >= 3:
    remove_guest = list.pop()
    print("So sorry my friend " + remove_guest + ", I will invite you next time"\
          + " to have lunch together.")

# print invitation again
message = "Why don't we have a lunch on May 5 " \
      + "at the Soka station?"
invite(list)

print(str(len(list)) + " friends will have lunch with you")

# remove the guest from list until it become null
del list[0:]
    
if list == []:
    print("the guest list is null now.")
else:
    print("the guest list isn't null now. May be there something wrong with the program."\
          + " please check your source code again")
    

