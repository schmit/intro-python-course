class Animal:
    def __init__(self, n_legs, color):
        self.n_legs = n_legs
        self.color = color

    def make_noise(self):
        print 'noise'