def is_prime(x):
    for i in xrange(2, x):
        if x % i == 0:
            return False
    return True