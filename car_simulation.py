import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Car Simulation")
clock = pygame.time.Clock()  # Create a clock object to control the frame rate

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define the Car class
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.max_speed = 2  # Slower max speed
        self.acceleration = 0.1  # Adjusted acceleration
        self.deceleration = 0.1  # Adjusted deceleration
        self.turn_speed = 5  # Adjusted turning speed for more noticeable turning

    def update(self, action):
        if action == 0:  # Accelerate
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif action == 1:  # Decelerate
            self.speed = max(self.speed - self.deceleration, -self.max_speed)
        elif action == 2:  # Turn left
            self.angle += self.turn_speed
        elif action == 3:  # Turn right
            self.angle -= self.turn_speed

        self.x += self.speed * math.sin(math.radians(self.angle))
        self.y -= self.speed * math.cos(math.radians(self.angle))

    def draw(self, window):
        car_surface = pygame.Surface((20, 10))
        car_surface.fill(red)
        rotated_car = pygame.transform.rotate(car_surface, self.angle)
        rect = rotated_car.get_rect(center=(self.x, self.y))
        window.blit(rotated_car, rect.topleft)

# Define the Track class
class Track:
    def __init__(self):
        self.track_lines = []

    def draw(self, window):
        for line in self.track_lines:
            pygame.draw.line(window, white, line[0], line[1], 2)

    def add_line(self, start, end):
        self.track_lines.append((start, end))
