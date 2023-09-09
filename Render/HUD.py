import pygame
import Utils.VecCG as VecCG
import Gen.WorldBuilder as WorldBuilder
import Registry

def fetchRects(keyDict):
    for key in keyDict:
        if keyDict[key] == True:
            key = str(key)
            if key.startswith('INFO'):
                yield drawInfoPane(key.partition('INFO')[2])

def drawInfoPane(key):
    if key == 'tileInfo':
        tile = WorldBuilder.Lvl.fetchTile(WorldBuilder.Lvl.sessionVar['mouseSelectedTile'])

        CENTERCONST = (0, 100)
        FONT = pygame.font.Font('freesansbold.ttf', 32)

        panelRect = pygame.Rect(0, 100, 9*32, 880)
        #, border_top_right_radius = 5, border_bottom_right_radius = 5)

        panelColor = (0, 0, 0, 100)
        panelTex = pygame.Surface((9*32, 880)).convert_alpha()
        panelTex.fill(panelColor)

        yield (panelTex, panelRect)


        text = FONT.render(tile.RTileInfo.name.upper(), True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = VecCG.Vector.sum(CENTERCONST, (9*16, 50))

        yield (text, textRect)

        tileTex = Registry.Textures[tile.RTileInfo.tex].convert_alpha()
        tileTex = pygame.transform.scale(tileTex, (5*32, 5*32))
        tileRect = pygame.Rect(CENTERCONST[0]+64, CENTERCONST[1] + 100, 5*32, 5*32)
        #,border_bottom_right_radius = -2, border_top_right_radius = -2, border_bottom_left_radius = -2, border_top_left_radius= -2)

        yield (tileTex, tileRect)
        
    elif key == 'posInfo':
        CENTERCONST = (1920/2-100, 0)
        FONT = pygame.font.Font('freesansbold.ttf', 10)

        panelRect = pygame.Rect(CENTERCONST[0], CENTERCONST[1], 150, 30)
        panelColor = (0, 0, 0, 100)
        panelTex = pygame.Surface((150, 30)).convert_alpha()
        panelTex.fill(panelColor)

        yield (panelTex, panelRect)

        text = str(WorldBuilder.Player.globalpos)[1:-1].partition(',')
        text = 'POS:  X: ' + text[0] + ' Y: ' + text[2]
        text += ' FPS: ' + str(WorldBuilder.Lvl.sessionVar['fps'])
        text = FONT.render(text, True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = VecCG.Vector.sum(CENTERCONST, (15, 15))

        yield (text, textRect)





