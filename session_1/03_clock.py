import pygame

pygame.init()

clock = pygame.time.Clock()

count = 0

while count < 20:
    print(count)

    count = count + 1

    clock.tick(10)

pygame.quit()
