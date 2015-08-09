class Range:
    def __init__(self, end, start=0, step=1):
        if end < start:
            end, start = start, end
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def next(self):
        c = self.current
        if c >= self.end:
            raise StopIteration
        self.current += self.step
        return c