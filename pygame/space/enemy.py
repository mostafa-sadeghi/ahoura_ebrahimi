from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        # self.bullet_group = bullet_group
        self.speed = 2
    def update(self):
        self.rect.x += self.direction * self.speed




