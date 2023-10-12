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

    def move(self):
        # TODO
        """
        در صورت وارد شدن شوالیه به داخل زمین بازی
        نتواند از ان خارج شود
        مگر با فشردن دکمه فاصله

        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocity
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity

    def escape(self):
        # TODO
        "بازیکن باید با فشردن دکمه فاصله بتواند به محل امن خود فرار کند"
        "محل امن بازیکن در پایین صفحه و در وسط قرار دارد"
        "نکته تعداد دفعاتی که بازیکن می تواند فرار کند دومرتبه است"
