import pygame
from enemy import Enemy
class Game:
    def __init__(self, player, enemy_group):
        self.score = 0
        self.round_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.font = pygame.font.Font("assets/Facon.ttf")
        self.new_round_sound = pygame.mixer.Sound("assets/new_round.wav")

    def draw(self, screen):
        pass

    def start_new_level(self):
        self.round_number += 1
        for i in range(7):
            for j in range(15):

                enemy = Enemy(j*64, i*64 + 100)
                self.enemy_group.add(enemy)



