def reducer(key, values):
    # key is a word string
    # values is a list of 1's corresponding
    #   to a mapper finding that word
    yield key, sum(values)