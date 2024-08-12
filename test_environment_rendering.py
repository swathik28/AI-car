import pygame
from car_simulation import Car, Track, window_width, window_height, window, black, clock

# Initialize Pygame
pygame.init()

# Create the car and track objects
car = Car(window_width // 2, window_height // 2)
track = Track()
track.add_line((100, 100), (700, 100))
track.add_line((700, 100), (700, 500))
track.add_line((700, 500), (100, 500))
track.add_line((100, 500), (100, 100))

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the car position (simple forward movement for testing)
    car.update(0)

    # Render the environment
    window.fill(black)
    track.draw(window)
    car.draw(window)
    pygame.display.update()
    clock.tick(30)  # Limit frame rate to 30 FPS

pygame.quit()
