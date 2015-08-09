# write elements of list to file
with open(filename, 'w') as f:
    for x in xs:
        f.write('{}\n'.format(x))

# write elements of dictionary to file
with open(filename, 'w') as f:
    for k, v in d.iteritems():
        f.write('{}: {}\n'.format(k, v))
