import re

pat = '\(?(\d{3})[-\)]?\s?(\d{3})[-\s]?(\d{4})$'
repat = re.compile(pat)
string = '(123) 456-7890'
search =  repat.search(string)
if search:
    print search.groups()
else:
    print 'not found'
