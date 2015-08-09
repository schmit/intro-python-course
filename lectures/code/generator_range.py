def myrange(end, start=0, step=1):
    if start > end:
        start, end = end, start
    current = start
    yield current
    while current+step < end:
        current += step
        yield current
