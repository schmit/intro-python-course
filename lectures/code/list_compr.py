ints = [1, 3, 10]

[i * 2 for i in ints]
# [2, 6, 20]

[[i, j] for i in ints for j in ints if i != j]
# [[1, 3], [1, 10], [3, 1], [3, 10], [10, 1], [10, 3]]

[(x, y) for x in xrange(3) for y in xrange(x+1)]
# ...
