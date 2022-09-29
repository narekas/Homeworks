# Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
print([x for x in range(100, 1001) if str(x) == str(x)[::-1]])
