import pygame
from config import *
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("monster_game/assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2
        self.velocity = 5
        self.lives = 3
        # تعداد دفعات فرارکردن بازیکن
        self.warps = 2
        self.catch_sound = pygame.mixer.Sound("monster_game/assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("monster_game/assets/die.wav")
        self.warp_sound = pygame.mixer.Sound("monster_game/assets/warp.wav")

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def reset(self):
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2
