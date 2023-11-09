from pygame.sprite import Sprite
import pygame
from constants import *


class Player(Sprite):
    def __init__(self, bullet_group):
        self.image = pygame.image.load("assets/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT
        self.bullet_group = bullet_group
        self.lives = 3

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        """فقط چپ و راست"""
        pass