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

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

    