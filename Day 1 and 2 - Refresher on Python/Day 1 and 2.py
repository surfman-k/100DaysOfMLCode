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


########################
### Exercise: Loops  ###
########################

### Simple For Loop
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

### Loop over every character in a string
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')  # HELLO

### Range of loop
for i in range(5):
    print("Doing important work. i =", i)
Doing important work. i = 0
Doing important work. i = 1
Doing important work. i = 2
Doing important work. i = 3
Doing important work. i = 4

### Enumerate
nums = [1, 2, 4, 8, 16]
def double_odds(nums):
    for i, num in enumerate(nums):
        if num % 2 == 1:
            nums[i] = num * 2

x = list(range(10))
double_odds(x)
x
# [0, 2, 2, 6, 4, 10, 6, 14, 8, 18]

### Iterating over Tuples
nums = [
    ('one', 1, 'I'),
    ('two', 2, 'II'),
    ('three', 3, 'III'),
    ('four', 4, 'IV'),
]

for word, integer, roman_numeral in nums:
    print(integer, word, roman_numeral, sep=' = ', end='; ')
1 = one = I; 2 = two = II; 3 = three = III; 4 = four = IV; 

### While Loop
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
0 1 2 3 4 5 6 7 8 9 

### List Comprehension
squares = [n**2 for n in range(10)]
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

