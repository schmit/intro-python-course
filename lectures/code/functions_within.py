def function1(x):
    def function2(y):
        print y + 2
        return y + 2

    return 3 * function2(x)

a = function1(2)    # 4
print a             # 12
b = function2(2.5)  # error: undefined name
