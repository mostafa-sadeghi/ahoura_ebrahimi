import pygame


pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
main_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))

# TODO define score variable
# TODO define lives variable

dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)
dragon_right_rect = dragon_right.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


player = pygame.transform.flip(pygame.image.load("player.png"), True, False)
player_rect = player.get_rect()
player_rect.midleft = (30, WINDOW_HEIGHT/2)

font = pygame.font.Font("myfont.ttf", 64)
title = font.render("Dragon Game", True, (0, 255, 0), (10, 50, 10))
title_rect = title.get_rect()
title_rect.center = (WINDOW_WIDTH/2, 30)

# TODO  render a text for score variable
# set score text position

# TODO  render a text for lives variable
# set lives text position


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

    main_surface.fill((0, 0, 0))

    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, dragon_right_rect)
    main_surface.blit(title, title_rect)
    # TODO blit score text and lives
    pygame.draw.line(main_surface, (255, 255, 255),
                     (0, 130), (WINDOW_WIDTH, 130), 5)
    main_surface.blit(player, player_rect)

    pygame.display.update()

pygame.quit()
