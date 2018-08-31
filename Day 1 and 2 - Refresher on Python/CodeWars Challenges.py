####################################
#### 6 kyu - Playing with digits ###
####################################

# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.
# Note: n, p will always be given as strictly positive integers.

### My Solution:

def dig_pow(n, p):
    result = 0
    for ind, digit in enumerate(str(n)):
        result += pow(int(digit),(ind+p))
    return result/n if result%n==0 else -1


####################################
#### 6 kyu - Your order, please  ###
####################################

# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

# your_order("is2 Thi1s T4est 3a")
# [1] "Thi1s is2 3a T4est"

### My Solution: (Terrible solution but at least I got there...)

def order(sentence):
  words = sentence.split(' ')
  final = []
  result = {}
  output = []
  numbers = ['1','2','3','4','5','6','7','8','9']
  ind = 0
  for val in words:  
      for letter in val:
          if letter in numbers:
              final.append(numbers.index(letter))
  for order in final:
      result[order] = words[ind]
      ind += 1
      
  for key, value in result.items():
      output.append(value)
      
  return " ".join(output)

# Here's a much cleaner solution... I have a lot of work to do

def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


############################
#### 7 kyu - Two to One  ###
############################

# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,

# each taken only once - coming from s1 or s2. #Examples: ``` a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
# a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```

def longest(s1, s2):
    s3 = (s1 + s2)
    listed = list(s3)
    listed.sort()
    final = []
    for lets in listed:
        if final.count(lets) == 0:
            final.append(lets)
    return ''.join(final)

def longest2(a1, a2):
    return "".join(sorted(set(a1 + a2)))


#####################################################
#### 7 kyu - Sum of two lowest positive integers  ###
#####################################################

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

# Hint: Do not modify the original array.

def sum_two_smallest_numbers(numbers):
  roted = sorted(numbers)
  return(roted[0] + roted[1])


###############################
#### 6 kyu - Who Likes It?  ###
###############################

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + " likes this"
    if len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    if len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if len(names) > 3:
        return names[0] + ", " + names[1] + " and " + str(len(names[2:])) + " others like this"