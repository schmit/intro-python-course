def reverse_list(xs):
    if len(xs) <= 1:
        return xs
    else:
        return reverse_list(xs[1:]) + [xs[0]]
