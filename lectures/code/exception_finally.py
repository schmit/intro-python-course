def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print 'Division by zero!'
    finally:
        print "Finally clause"

print div(3,2)
print div(3,0)
