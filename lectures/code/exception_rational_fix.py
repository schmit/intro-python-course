class Rational:
    def __init__(self, p, q=1):
        if q == 0:
            raise ZeroDivisionError('denominator is zero')
        g = gcd(p, q)
        self.p = p / g
        self.q = q / g