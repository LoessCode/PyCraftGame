class Pane():
    def __init__(self, pos, tiles):
        self.pos = pos
        self.tiles = tiles

class World():

    def __init__(self):
        self.World = {}

    
    #WorldManipulation functions
    def addPane(self, pane):
        #Adds a pane to the World. Used by WorldGen
        key = str(pane.pos)[1:-1]
        self.World[key] = pane
    def fetchPane(globalpos):
        pass

    def fetchTile(self, globalpos):
        import Utils.VecCG as VecCG

        tilePane = VecCG.Vector.cDiv(globalpos, 9)
        tileRelativePos = VecCG.Vector.findRelativePos(globalpos, VecCG.Vector.cMult(tilePane, 9))

        return self.World[str(tilePane)[1:-1]].tiles[tileRelativePos[1]][tileRelativePos[0]]
