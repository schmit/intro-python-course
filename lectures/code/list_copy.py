a = [1, 2, 3]
b = a  # let's copy a
print b

b[1] = 5  # now we want to change an element

print b
# [1, 5, 2]

print a
# [1, 5, 2]
