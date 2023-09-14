import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60
clock = pygame.time.Clock()

DOG_NORMAL_VELOCITY = 5
DOG_FAST_VELOCITY = 15
dog_velocity = DOG_NORMAL_VELOCITY

dog_left_image = pygame.image.load("assets/dog.png")
dog_right_image = pygame.transform.flip(dog_left_image, True, False)

dog_image = dog_right_image
dog_rect = dog_image.get_rect(
    topleft=(WINDOW_WIDTH/2 - 64, WINDOW_HEIGHT - 128))





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_rect.x -= dog_velocity
        dog_image = dog_left_image
    if keys[pygame.K_RIGHT]:
        dog_rect.x += dog_velocity
        dog_image = dog_right_image

    display_surface.fill((0, 0, 0))
    display_surface.blit(dog_image, dog_rect)
    pygame.display.update()
    clock.tick(FPS)
