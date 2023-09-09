import Gen.WorldBuilder as WorldBuilder
import pygame
import Utils.VecCG as VecCG
import json
import Render.Render as Render

with open(r"Data\Const.json", 'r') as Const:
    CENTERCONST = json.load(Const)['RENDER_CENTERCONST']

def keyDown(key):
    #Player Movement
    if key == pygame.K_w: WorldBuilder.movePlayer("w", 1)
    elif key == pygame.K_a: WorldBuilder.movePlayer("a", 1)
    elif key == pygame.K_s: WorldBuilder.movePlayer("s", 1)
    elif key == pygame.K_d: WorldBuilder.movePlayer("d", 1)

    elif key == pygame.K_i: WorldBuilder.Lvl.appendSessionVar('hud', 'INFOtileInfo')

    else: return 'ignore'

def mouseDown(pos, tileRects):

    pos = VecCG.Vector.sum(VecCG.Vector.sum(WorldBuilder.Player.globalpos,
     VecCG.Vector.cDiv(VecCG.Vector.findRelativePos(CENTERCONST, pos), 32)), (1, 1))

    if WorldBuilder.Lvl.sessionVar['mouseSelectedTile'] != pos:
        WorldBuilder.Lvl.updateSessionVar('mouseSelectedTile', pos, mode = 'tuple')
        WorldBuilder.Lvl.updateSessionVar('hud', True, valueKey = 'INFOtileInfo', mode = 'dict')
    else:
        WorldBuilder.Lvl.updateSessionVar('mouseSelectedTile', None, mode = 'tuple')
        WorldBuilder.Lvl.updateSessionVar('hud', False, valueKey= 'INFOtileInfo', mode = 'dict')

    
    
    


    