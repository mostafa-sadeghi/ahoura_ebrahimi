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

    def start_new_round(self):
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
