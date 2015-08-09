class Rational:
    def __init__(self, p, q=1):
        g = gcd(p, q)
        self.p = p / g
        self.q = q / g

    def __repr__(self):
        return '{}/{}'.format(p, q)