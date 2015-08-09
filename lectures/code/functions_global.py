x = 0

def incr_x():
    x = x + 1  # does not work

def incr_x2():
    global x
    x = x + 1  # does work
