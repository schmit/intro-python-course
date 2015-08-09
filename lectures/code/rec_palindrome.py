def is_palin(s):
    '''returns True iff s is a palindrome'''
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palin(s[1:-1])
