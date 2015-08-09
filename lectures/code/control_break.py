max_n = 10
for n in range(2, max_n):
    for x in range(2, n):
        if n % x == 0:  # n divisible by x
            print n, 'equals', x, '*', n/x
            break
    else:  # executed if no break in for loop
        # loop fell through without finding a factor
        print n, 'is a prime number'
