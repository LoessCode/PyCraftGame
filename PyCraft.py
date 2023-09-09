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

def update():
    Render.clear()
    Render.drawTiles()
    Render.drawHud()

    pygame.display.update()

running = True
update()

CLOCK = pygame.time.Clock()
while(running):

    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            Registry.dumpSavedGame(WorldBuilder.Player, WorldBuilder.Lvl)
            pygame.quit()
            quit()

        #Movement
        elif event.type == pygame.KEYDOWN:
            tval = InputHandler.keyDown(event.key)
            if tval != 'ignore':
                update()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            InputHandler.mouseDown(pygame.mouse.get_pos(), WorldBuilder.Lvl.renderedTiles)
            update()
 
    WorldBuilder.Lvl.updateSessionVar('fps', CLOCK.get_fps(), mode='tuple')
    dt = CLOCK.tick(60)
    #update() Drops frames to 9fps

        

