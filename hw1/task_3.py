# a program that asks the user to enter n number and prints the n-th Fibonacci number.

fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)  # ^-)

print(fib(int(input('Enter the number. '))))
