import pygame
from enemy import Enemy
from constants import *
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


    def update(self):
        self.check_collisions()

    def check_collisions(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
                on_edge = True
                break

        if on_edge:
            death = False
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += self.round_number * 5
                if enemy.rect.bottom >= SCREEN_HEIGHT - 100:
                    death = True
                    break
            if death:
                # TODO  ریست شدن بازی

            





