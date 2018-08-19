# Alien Game

# Create the dictionary
alien_0 = {}

# Add color and points
alien_0['color'] = 'green'
alien_0['points'] = 5

# add position x, y and speed
#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

# Move the alien to the right
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# New x_position
alien_0['x_position'] = alien_0['x_position'] + x_increment
alien_0
