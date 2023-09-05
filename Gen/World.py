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
