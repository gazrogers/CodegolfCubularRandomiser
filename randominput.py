import random

# Because of how we read the data in,
# the first index into the 3D array is the y-index (bottom layer first, top layer last),
# then the z-index (back first, front last),
# then the x-index (left first, right last)
def getinput():
  f = open('target.txt')
  lists = [list(z) for y in [x.split('\n') for x in f.read().split('\n\n')] for z in y]
  return [lists[i:i + 9] for i in xrange(0, len(lists), 9)]

def output(data):
  return '\n'.join([''.join(row) for layer in data for row in layer+['\n']])

print output(getinput())