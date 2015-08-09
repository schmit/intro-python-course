def f1():
    global x
    x = x + 1
    return x

def f2():
    return x + 1

def f3():
    x = 5
    return x + 1

x = 0
print f1() # output? x?
print f2() # output? x?
print f3() # output? x?