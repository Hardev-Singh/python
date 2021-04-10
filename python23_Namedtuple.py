# Namedtuple 

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55,155,255)
white = Color(255,20,55)

print(color.blue)
print(white.green)
# list / tuple
color = (55,155,255)

# dictionary
color = {'red': 55, 'green': 155, 'blue': 255}
print(color['red'])
