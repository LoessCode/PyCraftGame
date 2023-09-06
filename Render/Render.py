import pygame
import Gen.WorldBuilder as WorldBuilder
import Registry
import Utils.VecCG as VecCG
import random


global panel
panel = pygame.display.set_mode((1920, 1080))
CENTERCONST = (1920/2-16, 1080/2-16)


def init():
    pygame.init()
    panel = pygame.display.set_mode((1920, 1080))

def clear(): panel.fill((0, 0, 0))

def drawPlayer(pos, pane):
    
    playerTex = pygame.image.load(WorldBuilder.Player.tex).convert_alpha()

    playerRect = pygame.Rect((pos[0] * 32 + CENTERCONST[0]), (pos[1] * 32 + CENTERCONST[1]), 32, 32)

    panel.blit(playerTex, playerRect)

    pygame.display.update()


def drawTiles(work='*'):
    Player = WorldBuilder.Player; Lvl = WorldBuilder.Lvl
    quality = 'simple'; radius = 30

    posmatrix = [pos for pos in VecCG.areaPosMatrix(Player.globalpos, radius)]

    for pos in posmatrix:
        tilePane = VecCG.Vector.cDiv(pos, 9)
        tilePlayerRelativePos = VecCG.Vector.findRelativePos(Player.globalpos, pos)

        try:
            Lvl.World[str(tilePane)[1:-1]]
        except:
            WorldBuilder.GenPane(tilePane)

        tile = Lvl.fetchTile(pos)
        tileTex = Registry.Textures[tile.RTileInfo.tex].convert_alpha()

        
        tileRect = pygame.Rect(tilePlayerRelativePos[0]*32 + CENTERCONST[0], tilePlayerRelativePos[1]*32 + CENTERCONST[1], 32, 32)

        if quality == "real":
            panel.blit(tileTex, tileRect)

        elif quality == "simple":
            dist = VecCG.Vector.mod(Player.globalpos, pos) + 1

            """ Night time settings
            fogDist = 10
            maxRadius = radius*(2**.5)
            dropFactors = (2, 2)
            maxAlpha = 180
            """
            fogDist = 18
            maxRadius = radius*(2**.5)
            dropFactors = (.8, 0.6)
            maxAlpha = 255

            lVal = lambda dist: ((maxRadius - dist*dropFactors[0])/maxRadius) if ((fogDist+1)//dist) else (maxRadius/(maxRadius*(dist - fogDist + 1)**dropFactors[1]))


            tileTex.set_alpha(maxAlpha*lVal(dist))
            tileTex = pygame.transform.rotate(tileTex, tile.rotation)

            panel.blit(tileTex, tileRect)


    drawPlayer((0, 0), (0, 0))
    pygame.display.update()
        
        
        
    



