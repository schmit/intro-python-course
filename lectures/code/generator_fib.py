def fib(n):
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
        yield a

for elem in fib(10):
    print elem
