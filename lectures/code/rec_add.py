def add(a, b):
    if b == 0:
        # base case
        return a
    # recursive step
    return add(a, b-1) + 1
