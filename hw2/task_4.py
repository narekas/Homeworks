# A year is a leap year if it is divisible by 4,
# except that years divisible by 100 are not leap years unless they are also divisible by 400.
# Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.
n = int(input('Year = '))
c = 0
if n > 1600:
    for i in range(1600, n + 1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            c += 1
else:
    for i in range(n, 1601):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            c += 1
print(c)
