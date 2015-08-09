
maxDivisibleInt = 10
# minimum x is at least:
x = 2 * 3 * 5 * 7
found = False
while not found:
    for y in range(1, maxDivisibleInt+1):
        if x % y != 0:
            break
    else:
        print x
        found = True
    x += 2 * 3 * 5 * 7
