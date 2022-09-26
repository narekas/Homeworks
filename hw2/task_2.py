# Write a program that generates and prints 50 random integers, each between 3 and 6.

from random import randint

i = 50
while i > 0:
    print(randint(3, 6), end=' ')
    i -= 1
