import pygame
from constants import *
from player import Player
from game import Game

pygame.init()

player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)
clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
game = Game(my_player, enemy_group)

game.start_new_level()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0,0,0))
    my_player.draw(screen)
    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
