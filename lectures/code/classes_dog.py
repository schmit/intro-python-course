class Dog(Animal):
    def __init__(self, color, name):
        Animal.__init__(self, 4, color)
        self.name = name
    def make_noise(self):
        print self.name + ': ' + 'woof'

bird = Animal(2, 'white')
bird.make_noise()
# noise
brutus = Dog('black', 'Brutus')
brutus.make_noise()
# Brutus: woof
shelly = Dog('white', 'Shelly')
shelly.make_noise()
# Shelly: woof
