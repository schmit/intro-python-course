def trapezoid(f, a, b, N):
    '''integrates f over [a,b] using N steps'''
    if a > b:
        a, b = b, a
    # step size
    h = float(b-a)/N
    # running sum
    s = h/2 * (f(a) + f(b))
    for k in xrange(1, N-1):
        s += h * f(a + h*k)
    return s
