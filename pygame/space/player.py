from pygame.sprite import Sprite
import pygame
from constants import *
from playerbullet import PlayerBullet

class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT
        self.bullet_group = bullet_group
        self.lives = 3

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

    def fire(self):
        PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
