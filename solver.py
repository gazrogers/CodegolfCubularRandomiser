def getinput(filename):
    f = open(filename)
    cube = f.read()
    lists = [list(z) for y in [x.split('\n') for x in cube.split('\n\n')] for z in y]
    return [lists[i:i + 9] for i in xrange(0, len(lists), 9)]

cube = getinput('testinput.txt')
print cube

