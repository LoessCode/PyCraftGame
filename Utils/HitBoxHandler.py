import Utils.VecCG as VecCG

def isTouchingPaneBound(pos, dir): 
    return (True if pos[0]+dir[0]== -1 or pos[0]+dir[0] == 9 or pos[1]+dir[1] == -1 or pos[1]+dir[1] == 9 else False)

def getNextPanePos(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def getNextPanePlayerPos(pos, dir):
    if dir[0]: return (8 - pos[0], pos[1])
    else: return (pos[0], 8 - pos[1])

def isTouchingBarrier(dir, player, lvl):
    tilepos = VecCG.Vector.sum(player.globalpos, dir)
    tile = lvl.fetchTile(tilepos)

    if tile.RTileInfo.special["moveScope"] not in player.moveScope: return True
    else: return False