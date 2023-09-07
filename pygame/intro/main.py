import random
import pygame


pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
main_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))

score = 0
lives = 3

dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)
dragon_right_rect = dragon_right.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


player = pygame.transform.flip(pygame.image.load("player.png"), True, False)
player_rect = player.get_rect()
player_rect.midleft = (30, WINDOW_HEIGHT/2)

meat = pygame.image.load("meat.png")
meat_rect = meat.get_rect()
meat_rect.topleft = (
    WINDOW_WIDTH + 50, random.randint(140, WINDOW_HEIGHT - 64))


font = pygame.font.Font("myfont.ttf", 34)
title = font.render("Dragon Game", True, (0, 255, 0), (10, 50, 10))
title_rect = title.get_rect()
title_rect.center = (WINDOW_WIDTH/2, 30)


pygame.mixer.music.load("angry.mp3")
pygame.mixer.music.play(-1)


miss_sound = pygame.mixer.Sound("miss.mp3")
# TODO load catch sound

score_text = font.render(f"Score: {score}", True, (217, 10, 35))
score_rect = score_text.get_rect(center=(WINDOW_WIDTH/2, 70))

lives_text = font.render(f"lives: {lives}", True, (217, 10, 35))
lives_rect = lives_text.get_rect(center=(WINDOW_WIDTH/2, 100))

continue_text = font.render(
    f"Press any Key to continue ...", True, (217, 10, 35))
continue_rect = continue_text.get_rect(
    center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))


FPS = 60
clock = pygame.time.Clock()
meat_velocity = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 130:
        player_rect.y -= 5
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += 5

    score_text = font.render(f"Score: {score}", True, (217, 10, 35))
    lives_text = font.render(f"lives: {lives}", True, (217, 10, 35))

    main_surface.fill((0, 0, 0))

    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, dragon_right_rect)
    main_surface.blit(title, title_rect)
    main_surface.blit(meat, meat_rect)

    meat_rect.x -= meat_velocity
    if meat_rect.x <= 0:
        lives -= 1
        miss_sound.play()
        meat_rect.topleft = (
            WINDOW_WIDTH + 50, random.randint(140, WINDOW_HEIGHT
                                              - 64))

    if player_rect.colliderect(meat_rect):
        score += 1
        # play catch sound
        meat_rect.topleft = (
            WINDOW_WIDTH + 50, random.randint(140, WINDOW_HEIGHT
                                              - 64))

    if lives == 0:
        main_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        lives = 3
        score = 0

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    pygame.mixer.music.play()

                if event.type == pygame.QUIT:

                    is_paused = False
                    running = False

    pygame.draw.line(main_surface, (255, 255, 255),
                     (0, 130), (WINDOW_WIDTH, 130), 5)
    main_surface.blit(player, player_rect)
    main_surface.blit(score_text, score_rect)
    main_surface.blit(lives_text, lives_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
