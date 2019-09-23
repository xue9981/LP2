# First, create two list. One for confirm and another for store data
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# confirm every users and change all the confirmed list to confirmed_users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# display all the verified users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
