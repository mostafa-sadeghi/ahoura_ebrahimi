import pygame


SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
FPS = 60
CLOCK = pygame.time.Clock()
TILE_SIZE = 32
ROWS = SCREEN_HEIGHT // TILE_SIZE
COLS = SCREEN_WIDTH // TILE_SIZE

DIRT_IMG = pygame.image.load("assets/dirt.png")
GRASS_IMG = pygame.image.load("assets/grass.png")
WATER_IMG = pygame.image.load("assets/water.png")