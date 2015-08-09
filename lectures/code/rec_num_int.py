import math

def f(x):
    s = 100
    return math.exp(-s*x**2)

def trapezoid(f, a, b, N):
    if a > b:
        a, b = b, a
    h = float(b-a)/N
    s = h * (f(a) + f(b)) / 2.0
    for k in xrange(1, N):
        s += h * f(a + h*k)
    return s

# keep count of how many subintervals
count = 0
def adaptive_int(f, a, b, tol=1.0e-2, n=5, N=10):
    area = trapezoid(f, a, b, N)
    check = trapezoid(f, a, b, n)
    if abs(area - check) > tol:
        mid = (b + a) / 2.0
        area = adaptive_int(f, a, mid) + adaptive_int(f, mid, b)
    else:
        global count
        count += N
    return area

# integrate f from 0 to 3
print "trapezoid N = 10:     ", trapezoid(f, -3, 3, 10)
print "trapezoid N = 50:     ", trapezoid(f, -3, 3, 50)
print "trapezoid N = 100:    ", trapezoid(f, -3, 3, 100)
print "trapezoid N = 500:    ", trapezoid(f, -3, 3, 500)
print "trapezoid N = 5000:   ", trapezoid(f, -3, 3, 5000)
print "trapezoid N = 1000000:", trapezoid(f, -3, 3, 1000000)
print "trapezoid adaptive:   ", adaptive_int(f, -3, 3)
print count
