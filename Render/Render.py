import pygame
import Gen.WorldBuilder as WorldBuilder
import Registry
import Utils.VecCG as VecCG


global panel
panel = pygame.display.set_mode((1920, 1080))
CENTERCONST = (1920/2 - 16*9, 1080/2 - 16*9)


def init():
    pygame.init()
    panel = pygame.display.set_mode((1920, 1080))


def drawPlayer(pos, pane):
    
    playerTex = pygame.image.load(WorldBuilder.Player.tex).convert_alpha()

    playerRect = pygame.Rect((pos[0] * 32 + CENTERCONST[0]), (pos[1] * 32 + CENTERCONST[1]), 32, 32)

    panel.blit(playerTex, playerRect)

    pygame.display.update()


def drawPane(key, quality = "real", flag="nr", work="*", origin = (0, 0)):
    #for paneKey in World.Lvl.World:
    pane = WorldBuilder.Lvl.World[str(key)[1:-1]]
    ref = (VecCG.Vector.findRelativePos(key, origin) if flag == 'r' else (0, 0))
    print(ref)
    centerConst = (CENTERCONST[0] + ref[0]*32*9, CENTERCONST[1] + ref[1]*32*9)

    for tileRow in pane.tiles:
        for tile in tileRow:
            tileTex = Registry.Textures[tile.RTileInfo.tex].convert_alpha()
            #Here, 32 is the width and height of the rect.
            tileRect = pygame.Rect((tile.localpos[0] * 32 + centerConst[0]), (tile.localpos[1] * 32 + centerConst[1]), 32, 32)

            if quality == "real":
                panel.blit(tileTex, tileRect)
            elif quality == "simple":
                if flag == 'r':
                    centerTile = origin[0]*9 + 4, origin[1]*9 + 4 #Finding center tile to draw distance based fade
                    dist = (VecCG.Vector.mod(centerTile, tile.globalpos)/5)**3
                else: dist = 1
                color = [int(rgbval/dist) for rgbval in pygame.transform.average_color(tileTex)]
                color[-1] = 255
                tileTex.fill(color)
                panel.blit(tileTex, tileRect)


    if flag == "nr" and work == "*":
        drawFade(key)
    drawPlayer(WorldBuilder.Player.pos, pane)

    #pygame.display.update() # is done by drawPlayer.

def drawFade(key):
    posmatrix = [pos for pos in VecCG.areaPosMatrix(key, 1, flag='radial')]
    posmatrix.remove(posmatrix[4]) #Removing center pane as it is already rendered

    for pos in posmatrix: 
        if str(pos)[1:-1] in WorldBuilder.Lvl.World:
            drawPane(pos, flag="r", quality="simple", origin=key)
        else:
            WorldBuilder.GenPane(pos)
            drawPane(pos, flag="r", quality="simple", origin=key)

    fadeTex = pygame.image.load(r"Data\Assets\Hud\FadeMask.png")
    fadeRect = pygame.Rect(0, 0, 1920, 1080)

def drawTiles(work='*'):
    Player = WorldBuilder.Player; Lvl = WorldBuilder.Lvl
    quality = 'simple'; radius = 13

    posmatrix = [pos for pos in VecCG.areaPosMatrix(Player.globalpos, radius)]

    for pos in posmatrix:
        tilePane = VecCG.Vector.cDiv(pos, 9)
        tileRelativePos = VecCG.Vector.findRelativePos(pos, VecCG.Vector.cMult(tilePane, 9))

        try:
            Lvl.World[str(tilePane)[1:-1]]
        except:
            WorldBuilder.GenPane(tilePane)

        tile = Lvl.World[str(tilePane)[1:-1]].tiles[tileRelativePos[0]][tileRelativePos[1]] #[VecCG.Vector.findRelativePos((playerPane[0]*9, playerPane[1]*9), playerTile)]
        tileTex = Registry.Textures[tile.RTileInfo.tex].convert_alpha()

        
        tileRect = pygame.Rect(tileRelativePos[0] + CENTERCONST[0], tileRelativePos[1] + CENTERCONST[1], 32, 32)

        if quality == "real":
            panel.blit(tileTex, tileRect)

        elif quality == "simple":
            dist = 1 #(VecCG.Vector.mod(Player.globalpos, pos)/10)

            color = [int(rgbval/dist) for rgbval in pygame.transform.average_color(tileTex)]
            color[-1] = 255 #Alpha

            tileTex.fill(color)
            panel.blit(tileTex, tileRect)
    pygame.display.update()
        
        
        
    



def Clear(): panel.fill((0, 0, 0))