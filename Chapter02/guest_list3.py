# guests list
list = ['watanabe', 'turuoka', 'nakatani']

# print invitation
for name in list:
    print("Hello, " + name.title() + "!")

print("Why don't we have a lunch on May 5 " \
      + "at the Soka station?")

# print updated news
print("\n\t---News---")

# people to remove from guest list
old_guest = "turuoka"
# people to add in guest list 
new_guest = "sirahige"

# print updated news
print("Because " + old_guest.title() + " have someting to do on May 5, " + new_guest.title() + " will come on lunch on May 5 in alternitive.")

# remove old_guest form list
list.remove(old_guest)
# add new_guest in list
list.append(new_guest)

print(list)

# update news
print("\t\t\t---News---")
print("Because I found a larger restaurant, "\
      + "I determined to change the restaurant, and will invite more three guest to the lunch")

# the new guest to invite
new_guest1 = "hasimoto"
new_guest2 = "nagi"
new_guest3 = "senoue"

print(list)
# add new guest to the list
list.insert(0, new_guest1)
list.insert((list.__len__() // 2), new_guest2)
list.append(new_guest3)

print(list)

# print invitation
for name in list:
    print("Hello, " + name.title() + "!")

print("Why don't we have a lunch on May 5 " \
      + "at the Soka station?")
