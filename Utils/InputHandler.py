import Gen.WorldBuilder as WorldBuilder
import pygame

def keyDown(key):
    #Player Movement
    if key == pygame.K_w: WorldBuilder.movePlayer("w", 1); return 2
    elif key == pygame.K_a: WorldBuilder.movePlayer("a", 1); return 2
    elif key == pygame.K_s: WorldBuilder.movePlayer("s", 1); return 2
    elif key == pygame.K_d: WorldBuilder.movePlayer("d", 1); return 2

    return 0
