class Leaf:
    n_leafs = 0  # class attribute: shared

    def __init__(self, color):
        self.color = color  # object attribute
        Leaf.n_leafs += 1

redleaf = Leaf('red')
blueleaf = Leaf('blue')

print redleaf.color
# red
print Leaf.n_leafs
# 2
