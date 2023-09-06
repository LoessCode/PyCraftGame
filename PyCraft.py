import Gen.WorldBuilder as WorldBuilder
import Class.Entity as Entity
import pygame
import Registry
import Render.Render as Render
import Utils.InputHandler as InputHandler
import Utils.VecCG


#Registers all items and tiles from local Data
Registry.RegisterAll()
Registry.loadSavedGame()

#Initiates World-Gen module
WorldBuilder.init()
Player = WorldBuilder.Player

#Initiates the Render module
Render.init()

def update(scope = 9): #Defines how much to update. Optimisation.
    Render.clear()
    if scope > 2:
        Render.drawTiles()
    elif scope == 2:
        Render.drawTiles()
    elif scope == 1:
        Render.drawTiles()
        #Render.drawPane(WorldBuilder.Player.pane, work='lazy', quality='simple')
    

update()
running = True
while(running):
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            Registry.dumpSavedGame(WorldBuilder.Player, WorldBuilder.Lvl)
            pygame.quit()
            quit()

        #Movement
        elif event.type == pygame.KEYDOWN:
            update(InputHandler.keyDown(event.key))

            if event.key == pygame.K_0: print([tile.globalpos for tile in WorldBuilder.Lvl.World['-1, 0'].tiles[1]])

    #input("1")

    #pygame.display.update()
