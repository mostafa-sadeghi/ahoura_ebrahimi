import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT, ROWS, COLS,TILE_SIZE

class World:
    def __init__(self):
        bg_img = pygame.image.load("assets/background.png")
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH,SCREEN_HEIGHT))
        self.bg_rect = self.bg_img.get_rect(topleft=(0,0))


    def draw_bg(self, screen):
        screen.blit(self.bg_img, self.bg_rect)
        for row in range(ROWS):
            pygame.draw.line(screen,(255,0,0), (0, row * TILE_SIZE), (SCREEN_WIDTH, row * TILE_SIZE))
        for col in range(COLS):
            pygame.draw.line(screen,(255,0,0), (col * TILE_SIZE, 0), (col * TILE_SIZE,SCREEN_HEIGHT))



