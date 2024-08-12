import pygame

pygame.init()
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pygame Test")

black = (0, 0, 0)
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(black)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
