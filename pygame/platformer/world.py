import pygame
from constants import *

class World:
    def __init__(self, data):
        self.tile_map = []
        bg_img = pygame.image.load("assets/background.png")
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH,SCREEN_HEIGHT))
        self.bg_rect = self.bg_img.get_rect(topleft=(0,0))
      
        for row in range(len(data)):
           
            for col in range(len(data[row])):
                if data[row][col] == 1:
                    img = DIRT_IMG
                    rect = img.get_rect()
                    rect.topleft = (col * TILE_SIZE, row*TILE_SIZE)
                    self.tile_map.append((img, rect))
                if data[row][col] == 2:
                    img = GRASS_IMG
                    rect = img.get_rect()
                    rect.topleft = (col * TILE_SIZE, row*TILE_SIZE)
                    self.tile_map.append((img, rect))
                if data[row][col] == 3:
                    img = WATER_IMG
                    rect = img.get_rect()
                    rect.topleft = (col * TILE_SIZE, row*TILE_SIZE)
                    self.tile_map.append((img, rect))
                






    def draw_bg(self, screen):
        screen.blit(self.bg_img, self.bg_rect)
        # for row in range(ROWS):
        #     pygame.draw.line(screen,(255,0,0), (0, row * TILE_SIZE), (SCREEN_WIDTH, row * TILE_SIZE))
        # for col in range(COLS):
        #     pygame.draw.line(screen,(255,0,0), (col * TILE_SIZE, 0), (col * TILE_SIZE,SCREEN_HEIGHT))

        for tile in self.tile_map:
            screen.blit(tile[0], tile[1])




