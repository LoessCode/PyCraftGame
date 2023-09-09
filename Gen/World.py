class Pane():
    def __init__(self, pos, tiles):
        self.pos = pos
        self.tiles = tiles

class World():

    def __init__(self):
        self.World = {}
        self.renderedTiles = []
        self.sessionVar = {
            "hud": {
                'INFOtileInfo': False,
                'INFOposInfo': True
            },
            "mouseSelectedTile": (0, 0),
            "fps": 0
        }

    
    #WorldManipulation functions
    def addPane(self, pane):
        #Adds a pane to the World. Used by WorldGen
        key = str(pane.pos)[1:-1]
        self.World[key] = pane
    def fetchPane(globalpos):
        pass

    def fetchTile(self, globalpos, flag = 'tile'):
        import Utils.VecCG as VecCG

        tilePane = VecCG.Vector.cDiv(globalpos, 9)
        tileRelativePos = VecCG.Vector.findRelativePos(globalpos, VecCG.Vector.cMult(tilePane, 9))

        try: self.World[str(tilePane)[1:-1]]
        except:
            import Gen.WorldBuilder
            Gen.WorldBuilder.GenPane(tilePane)

        if flag == '':
            return (tilePane, tileRelativePos)         
        else:
            return self.World[str(tilePane)[1:-1]].tiles[tileRelativePos[1]][tileRelativePos[0]]


    def setRenderedTiles(self, tileRects):
        self.renderedTiles = tileRects
    
    def setTile(self, pos, tile):
        indexes = self.fetchTile(pos, flag = '')
        tiles = self.World[str(indexes[0])[1:-1]].tiles

        tiles[indexes[1][1]][indexes[1][0]] = tile
        self.addPane(Pane(indexes[0], tiles))

    def updateSessionVar(self, key, value, valueKey = None, mode=None):
        if mode == 'dict':
            self.sessionVar[key][valueKey] = value

        elif mode == 'tuple':
            self.sessionVar[key] = value
        
    
    def appendSessionVar(self, key, value):
        if value not in self.sessionVar[key]:
            self.sessionVar[key].append(value)
        else:
            self.updateSessionVar(key, value)


