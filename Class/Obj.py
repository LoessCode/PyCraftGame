class Tile():
    def __init__(self, RTileInfo, pos, pane):
        self.RTileInfo = RTileInfo
        self.localpos = pos
        self.globalpos = (pos[0] + pane[0]*9, pos[1] + pane[1]*9)
        self.pane = pane
        self.rotation = 360

    def setRotation(self, r):
        self.rotation = r
    