def func(x, a=1, b=3):
    return x + a - b

print func(2)       # 0
print func(5, 2)    # 4
print func(3, b=0)  # 4
