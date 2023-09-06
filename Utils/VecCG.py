class Vector():
    def __init__(origin, result, magnitude):
        self.origin = origin
        self.mod = mod(origin, head)
        self.head = result
    
    def mod(origin, head):
        x, y = origin[0] - head[0], origin[1] - head[1]
        return (x**2 + y**2)**.5

    def findRelativePos(pos1, pos2):
        x, y = pos1[0] - pos2[0], pos1[1] - pos2[1]
        return (x, y)

    def sum(pos1, pos2):
        x, y = pos1[0] + pos2[0], pos1[1] + pos2[1]
        return (x, y)

    def cMult(pos, const):
        x, y = pos[0]*const, pos[1]*const
        return(x, y)

    def cDiv(pos, const, flag = 'floor'): #Multiply by constant
        if flag == 'real':
            x, y = pos[0]/const, pos[1]/const
        else:
            x, y = pos[0]//const, pos[1]//const
        return (x, y)

def areaPosMatrix(origin, radius, flag = "radial"):
    if flag == 'radial':
        origin = (origin[0] - radius, origin[1] - radius)
        for x in range(2*radius+1):
            for y in range(2*radius+1):
                yield (origin[0] + x, origin[1] + y)
    elif flag == 'axial':
        for x in range(radius):
            for y in range(radius):
                yield (origin[0] + x, origin[1] + y)
