
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

    def setPos(self, pos):
        import Utils.VecCG as VecCG

        self.pane = VecCG.Vector.cDiv(pos, 9)
        self.globalpos = pos
        self.pos = VecCG.Vector.findRelativePos(VecCG.Vector.cMult(self.pane, 9), pos)
