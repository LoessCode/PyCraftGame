class Tile():
    def __init__(self, RTileInfo, pos, pane):
        self.RTileInfo = RTileInfo
        self.localpos = pos
        self.globalpos = (pos[0] + pane[0]*9, pos[1] + pane[1]*9)
        self.pane = pane
        self.rotation = 360
        self.specificAttr = {}

    def setRotation(self, r):
        self.rotation = r

    def setAttr(self, attrs = {}, flag = None):
        if flag == 'specificAttr':
            for attr in attrs:
                self.specificAttr[attr] = attrs[attr]
        return self