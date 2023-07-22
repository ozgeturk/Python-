x = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
count = 1
print(x, end=" ")
while x != 1 and x != 0:
    if x % 2 == 0:
        if count < 20:
            x = x // 2
            count += 1
            print(x, end=" ")
        else:
            break

    elif x % 2 == 1:
        if count < 20:
            x = (x * 3) + 1
            count += 1
            print(x, end=" ")
        else:
            break

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

"""
Cmpe150 Spring2021 Demo Final Question 1

Write a program that takes a positive integer x and then prints the related sequence until 1 or 0 is reached. The sequence is as follows: If the number is even, divide it by 2; if the number is odd, multiply it by 3 and add 1. Cut the sequence at 20 numbers even if it doesn't reach 1 or 0.

Note: Use integer division.

Note 2: Print the numbers in the sequence next to each other separated with a space. Do not print each number to a new line.

Note 3: You don't need to check whether the entered number is positive or not.

INPUT	OUTPUT
20	20 10 5 16 8 4 2 1
41	41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137
"""