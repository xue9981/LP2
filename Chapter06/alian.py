alien_0 = {'color':'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# the alien move to right
# the alien's speed will determine how long the alien will move

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this alien's speed must be high
    x_increment = 3

# new position will be calculated from old position
alien_0['x_position']+=x_increment

print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


