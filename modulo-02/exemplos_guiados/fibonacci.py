def fib(n):
    if n < 3:
        return n
    return fib(n - 1) + fib(n - 3) 

print([fib(i) for i in range(25)])