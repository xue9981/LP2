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
