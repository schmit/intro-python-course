def is_prime_fast(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    k = 6
    while k-1 < n ** 0.5:
        if n % (k - 1) == 0 or n % (k+1) == 0:
            return False
        k += 6
    return True
