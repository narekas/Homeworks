# Write a program that finds all four of the perfect numbers that are less than 1000.

for i in range(2, 1001):
    c = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            c += j
    if c == i:
        print(i)