import pygame
from random import randint
from monster import Monster
from config import *


class Game:
    def __init__(self, player, monster_group):
        self.player = player
        self.monster_group = monster_group
        self.score = 0
        self.round_number = 0

        self.font = pygame.font.Font("monster_game/assets/Abrushow.ttf")

        blue_monster = pygame.image.load(
            "monster_game/assets/blue_monster.png")
        green_monster = pygame.image.load(
            "monster_game/assets/green_monster.png")
        purple_monster = pygame.image.load(
            "monster_game/assets/purple_monster.png")
        yellow_monster = pygame.image.load(
            "monster_game/assets/yellow_monster.png")
        self.monsters_images = [blue_monster,
                                green_monster, purple_monster, yellow_monster]

        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.monsters_images[self.target_monster_type]
        self.target_monster_image_rect = self.target_monster_image.get_rect()
        self.target_monster_image_rect.centerx = WINDOW_WIDTH/2
        self.target_monster_image_rect.bottom = 100

    def draw(self, screen):
        """
        draw the game states and the target monster
        : screen
        """
        COLORS = (
            (14, 171, 231),
            (95, 213, 50),
            (238, 86, 252),
            (245, 177, 18)
        )
        # TODO
        # display score and player lives and round number and player warps number
        screen.blit(self.target_monster_image, self.target_monster_image_rect)
        pygame.draw.rect(screen, COLORS[self.target_monster_type],
                         (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 4)

    def start_new_round(self):
        """
        starts new round and spawn or create 
        """
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.monsters_images[0], 0))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.monsters_images[1], 1))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.monsters_images[2], 2))
            self.monster_group.add(Monster(randint(
                0, WINDOW_WIDTH - 64), randint(100, WINDOW_HEIGHT-164), self.monsters_images[3], 3))

    def update(self):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 1
                collided_monster.remove(self.monster_group)
