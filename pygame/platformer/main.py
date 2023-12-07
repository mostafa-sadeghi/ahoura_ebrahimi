from pygame.locals import *
from constants import *
from world import World
from levels.level1 import world_data

game_world = World(world_data)
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    game_world.draw_bg(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)