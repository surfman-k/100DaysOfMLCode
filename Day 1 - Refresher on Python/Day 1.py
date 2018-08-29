################################################
### Exercise: Syntax, Variables, and Numbers ###
################################################

### Simple variable declerations
color = "blue"
print('color', color)
odds = evens = []
print('odds', odds)
print('evens', evens)

### Simple math
pi = 3.14159 # approximate
diameter = 3
# Create a variable called 'radius' equal to half the diameter
radius = 1.5
# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi*(radius*radius)
print('area', a

### Swapping variable values
a = [1, 2, 3]
b = [3, 2, 1]

a, b = b, a

### Ninety-nine dashes
even = 7------3
odd = 7-----3
# even = 10
# odd = 4 


###########################
### Exercise: Functions ###
###########################

### Basic Functions
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    3.14
    """
    return round(num, 2)

print(round_to_two_places(3.14159)

### Time
from time import time
t = time()
print(t, "seconds since the Epoch

### Timeouts
from time import sleep
duration = 5
print("Getting sleepy. See you in", duration, "seconds")
sleep(duration)
print("I'm back. What did I miss?")


###########################
### Exercise: Booleans  ###
###########################

### Simple If/Else
def sign(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1


########################
### Exercise: Lists  ###
########################

### Lists are Python's equivalent to JS Arrays
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

### Slicing 
planets[0:3]
# ['Mercury', 'Venus', 'Earth']

### List Functions
len(planets)
sorted(planets)
sum(primes)
max(primes)

### List Methods
planets.append('Pluto')
planets.pop()
planets.index('Earth')
"Earth" in planets # Will return true if Earth is part of planets List

### Tuples
t = (1, 2, 3) # Like lists but cannot be modified



