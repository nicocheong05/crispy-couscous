def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(2))

# fib(n) returns the sum nth fibonacci numbers
# fibonacci sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
# a fibonacci number is the sum of the previous 2 fibonacci numbers
# i.e. fib(n) = fib(n-1) + fib(n-2)
