# Write a program that asks the user to enter two numbers, x and y , and computes | x − y | /  x+y
x, y = map(int, input('Enter the number x and y. ').split())
print(abs(x - y) / x + y)
