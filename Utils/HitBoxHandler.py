def isTouchingPaneBound(pos, dir): 
    return (True if pos[0]+dir[0]== -1 or pos[0]+dir[0] == 9 or pos[1]+dir[1] == -1 or pos[1]+dir[1] == 9 else False)

def getNextPanePos(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def getNextPanePlayerPos(pos, dir):
    if dir[0]: return (8 - pos[0], pos[1])
    else: return (pos[0], 8 - pos[1])

def isTouchingBarrier(pos, dir, player, lvl):
    tilePos = (pos[0] + dir[0], pos[1] + dir[1])

    if tilePos[0] > 8 or tilePos[0] < 0 or tilePos[1] > 8 or tilePos[1] < 0:
        pane = lvl.World[str(getNextPanePos(player.pane, dir))[1:-1]]
        tilePos = getNextPanePlayerPos(pos, dir)
    else:
        pane = lvl.World[str(player.pane)[1:-1]]

    for tilerow in pane.tiles:
        for tile in tilerow:
            if tile.localpos[0] == tilePos[0] and tile.localpos[1] == tilePos[1]: tile1 = tile;

    if tile1.RTileInfo.special["moveScope"] not in player.moveScope: return True
    else: return False