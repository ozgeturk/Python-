"""
counter = 0

for num in [1, 2, 3, 4, 5, 6]:
    print(num, end="\n") # use 'end' to move cursor to the next line with \n num, or ıf ı want to give spaces btw numbers ı can write end=" ".
    counter = counter + 1
print() # with this cursor moves to the next line.
print("The number of items is", counter)


###

largest_so_far = None

for num in [9, 41, 12, 3, 74, 15]:
    if largest_so_far is None: # is stronger than equal. "is" means same object
        largest_so_far = num
    elif num > largest_so_far:
        largest_so_far = num

print("The largest number is", largest_so_far)
"""

###
"""
total = 0
count = 0
average = 0

while True:
    user_input = input("Enter a number: ")

    if user_input == "done":
        break

    else:
        try:
            user_input = int(user_input)
            total += user_input
            count += 1
        except:
            print("Invalid input")
            continue

print(total, count, total/count)
"""
###
"""
user_input = input("Enter height: ")

user_input = int(user_input)

for i in range(user_input): # from 0 to "user_input - 1"
    for j in range(i+1):
        print("*", end="") # with end you dont move to the next line if we dont leave any space we see starts in a concatinating way.
    print()
"""
###
"""
N, K = map(int, input().split())

i = N
while i <= K:
    print(i, end=" ")
    i += 1
"""
###
"""
A, B, T = map(int, input().split())
i = A
while i <= B:
    print(i, end = " ")
    i += T
"""

###
"""
A, B = map(int, input().split())

i = A
sum = 0

while i <= B:
    if i % 2 == 0:
        sum += i
        i += 1
    else:
        i += 1
        continue
print(sum)
"""

###
"""
N = int(input())
sum = 0
count = 0
for i in range(N):
    new_input = int(input())
    sum += new_input
    count += 1
print(sum/count)
"""

###
"""
a, b = map(int, input().split())
product = 1 # it cannot be 0 because when I multıply it with a it willa lways be equal to 0.
i = a

for i in range(b):
    product = product * a
print(product)
"""

###
"""
N = int(input()) # assume 5


a = 0 # 1st
b = 1 # 2nd
print(a)
print(b)

# i = 3, 4, 5
for i in range(3, N+1):
     c = a + b
     print(c)
"""

####
# Queston 7 - SECOND LARGEST
"""
number = int(input())

largest = 0
second_largest = 0

while number != 0:
     if number > largest:
          second_largest = largest
          largest = number
     elif number > second_largest:
          second_largest = number
     number = int(input())
     
print("Largest", largest)
print("Second Largest", second_largest)
"""

####

# QUESTION 8 DIGITTSS
"""
number = int(input())
count = 0
even_sum = 0

# num = 24685
"""
"""
print(number % 10) # 123 % 10 = 3
number = num // 10 # 123 // 10 = 12
print(number % 10) # 12 % 10 = 2
number = number // 10 # 12 // 10 = 1
print(number % 10) # 1 % 10 = 1
"""
""""
while number != 0:
     digit = number % 10
     if digit % 2 == 0:
          even_sum += digit
     number = number // 10
     count += 1

print("Total digit count", count)
print("Even digit sum", even_sum)
"""

###
# QUESTION 9 - Positive Mental Attitude
"""
number = int(input()) # 1
odd_sum = 0

while number >= 0:
     if number % 2 != 0:
          odd_sum += number
     number = int(input())

print(odd_sum)
"""

###
# Question 10 - GUESS
"""
from random import randint

real_number = randint(1, 100)
# print(number)
guessed_number = int(input())
num_tries = 0
while guessed_number != real_number:
     if guessed_number > real_number:
          print("Too high!")
          num_tries += 1
          guessed_number = int(input())
     else:
          print("Too low!")
          num_tries += 1
          guessed_number = int(input())

else:
     num_tries += 1
     print("You got it! \n And it only took you", num_tries, "tries!")
"""
####
# Question 11 - NoBig
"""
count = 0
total_sum = 0

prev = int(input())
total_sum += prev
count += 1

while True:
     current = int(input())
     if current > prev:
          break
     else:
          total_sum += current
          count += 1
          prev = current
print(total_sum / count)
"""
###
# QUESTION 13 - greatest common divisor
"""
a, b = map(int, input().split())

# a = 18, b = 6
# gcd = 6
# i = 1 ... 6
if a > b:
     small = b
else:
     small = a

for i in range(1, small + 1):
     if a % i == 0 and b % i == 0:
          gcd = i

print(gcd)
"""
###
# QUESTION 14 - Disarium
number = int(input())
n = number # we store our number in another variable, so that we don't lost our number.
length = len(str(number))
disarium_sum = 0

while number > 0:
     digit = number % 10
     disarium_sum += digit ** length
     length -= 1
     number = number // 10


if disarium_sum == n:
     print(True)
else:
     print(False)

