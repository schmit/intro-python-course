class Fib:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def next(self):
        if self.i >= self.n: raise StopIteration
        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a
