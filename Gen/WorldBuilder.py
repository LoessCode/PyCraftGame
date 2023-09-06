from Gen.World import *
import Class.Entity as Entity
import Gen.GenEngine as GenEngine
import Utils.HitBoxHandler as HitBoxHandler
import Registry
import random
import Utils.VecCG as VecCG

boardRadius = 9

def init():
    global Lvl, Player
    if Registry.Save[0] == "!":
        Lvl = World()
        Player = Entity.Player()
        GenPane((0, 0))
    else:
        Lvl = Registry.Save[1]
        Player = Registry.Save[0]
        GenPane(Player.pos)

    

def GenPane(pos):
    tiles = GenEngine.genTiles(pos)
    Lvl.addPane(Pane(pos, tiles))

def movePlayer(dir, distance=1):
    dirKey = {"w": (0, 1), "a": (1, 0), "s": (0, -1), "d": (-1, 0)}
    dir = dirKey[dir]
    
    #Position of next pane and player in said plane
    nextPane = HitBoxHandler.getNextPanePos(Player.pane, dir)
    nextPanePlayerPos = HitBoxHandler.getNextPanePlayerPos(Player.pos, dir)

    if HitBoxHandler.isTouchingBarrier(dir, Player, Lvl):
        pass
    else:
        Player.setPos(VecCG.Vector.sum(Player.globalpos, dir))


