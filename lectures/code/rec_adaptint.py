def ada_int(f, a, b, tol=1.0e-6, n=5, N=10):
    area = trapezoid(f, a, b, N)
    check = trapezoid(f, a, b, n)
    if abs(area - check) > tol:
        # bad accuracy, add more points to interval
        m = (b + a) / 2.0
        area = ada_int(f, a, m) + ada_int(f, m, b)
    return area
