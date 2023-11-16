from pygame.sprite import Sprite
import pygame

class PlayerBullet(Sprite):
    def __init__(self, x,y , bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/green_laser.png")
        self.rect = self.image.get_rect(centerx = x, bottom =y)
        bullet_group.add(self)

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom <= 0:
            self.kill()