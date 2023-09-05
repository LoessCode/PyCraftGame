import Utils.VecCG

class Player():
    def __init__(self):
        self.pos = [4, 4]

        #Player Inventory Dict
        self.inv = {
            "matRaw": [],
            "toolRock": [],
            "toolSplit": [],
            "toolHurt": []
        }

        self.tex = "Data/Assets/Entity/Player.png"
        self.pane = (0, 0)
        self.moveScope = [0]
        self.globalpos = (0, 0)

    def setPos(self, pos, pane = 0):
        deltaPos = VecCG.Vector.findRelativePos(self.pos, pos)
        self.globalpos = (self.globalpos[0] + deltaPos[0], self.globalpos[1] + deltaPos[1])
        print(self.globalpos)
        self.pos = pos
        self.pane = (self.pane if pane == 0 else pane)