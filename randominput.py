import random

target = [[['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']], [['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9']], [['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1']], [['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2']], [['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3']], [['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4']], [['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5']], [['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6']], [['9', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['8', '9', '1', '2', '3', '4', '5', '6', '7']]]

# Because of how we read the data in,
# the first index into the 3D array is the y-index (bottom layer first, top layer last),
# then the z-index (back first, front last),
# then the x-index (left first, right last)
def getinput(filename):
    f = open(filename)
    string = f.read().split('\n\n')
    cube = '\n\n'.join(string[:-1])
    solution = string[-1]
    lists = [list(z) for y in [x.split('\n') for x in cube.split('\n\n')] for z in y]
    return [[lists[i:i + 9] for i in xrange(0, len(lists), 9)], solution]

def output(data):
    return '\n'.join([''.join(row) for layer in data for row in layer+[[]]])

def getsubcube(cube, x, y, z):
    x = clamp(x, 1, 7)
    y = clamp(y, 1, 7)
    z = clamp(z, 1, 7)
    return [[[char for char in row[x-1:x+2]] for row in layer[z-1:z+2]] for layer in cube[y-1:y+2]]

def replacesubcube(cube, subcube, x, y, z):
    newcube = cube
    for ypos in range(y-1, y+2):
        for zpos in range(z-1, z+2):
            for xpos in range(x-1, x+2):
                newcube[ypos][zpos][xpos] = subcube[ypos-y+1][zpos-z+1][xpos-x+1]
    return newcube

def clamp(n, minn, maxn):
    return max(min(n, maxn), minn)

def rotateX(cube, n):
    newcube = cube
    for _ in range(n):
        newcube = [
            [newcube[2][0], newcube[1][0], newcube[0][0]],
            [newcube[2][1], newcube[1][1], newcube[0][1]],
            [newcube[2][2], newcube[1][2], newcube[0][2]]
        ]
    return newcube

# algorithm shamelessly stolen from http://stackoverflow.com/a/496056/618347
def rotateY(cube, n):
    newcube = cube
    for _ in range(n):
        newcube = [zip(*x)[::-1] for x in newcube]
    return newcube

# Easier to define in terms of rotateX and rotateY
def rotateZ(cube, n):
    newcube = cube
    for _ in range(n):
        newcube = rotateY(rotateX(rotateY(newcube, 1), 3), 3)
    return newcube

def randomisecube(cube):
    newcube = cube
    generator = ""
    solution = ""
    funclist = [[rotateX, "X"], [rotateY, "Y"], [rotateZ, "Z"]]
    for _ in range(random.randint(10, 100)):
        x = random.randint(1, 7)
        y = random.randint(1, 7)
        z = random.randint(1, 7)
        rotateFunc = random.choice(funclist)
        numRots = random.randint(1,3)
        subcube = getsubcube(newcube, x, y, z)
        subcube = rotateFunc[0](subcube, numRots)
        newcube = replacesubcube(newcube, subcube, x, y, z)
        generator = generator + str(x) + str(y) + str(z) + rotateFunc[1] + str(numRots) + '\n'
        solution = str(x) + str(y) + str(z) + rotateFunc[1] + str(4-numRots) +'\n' + solution
    return [generator, solution, newcube]

def verifysolution(cube, solution):
    newcube = cube
    funclist = {"X": rotateX, "Y": rotateY, "Z": rotateZ}
    for move in solution.split('\n'):
        movelist = list(move)
        subcube = getsubcube(newcube, int(movelist[0]), int(movelist[1]), int(movelist[2]))
        subcube = funclist[movelist[3]](subcube, int(movelist[4]))
        newcube = replacesubcube(newcube, subcube, int(movelist[0]), int(movelist[1]), int(movelist[2]))
    return newcube == target

# Code to generaterandom cubes - Uncomment/Comment as necessary
answer = randomisecube(target)
print "Cube:"
print output(answer[2])
print "Generated by:"
print answer[0]
print "Possible solution:"
print answer[1]

# Code to verify solution - Uncomment/Comment as necessary
# [cube, solution] = getinput('testsolution.txt')
# print verifysolution(cube, solution)
