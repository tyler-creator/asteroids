import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        velocity = pygame.Vector2(0,0)
        position = pygame.Vector2(x,y)
        super().__init__(position, velocity, radius)        

    def draw(self, screen):
        position = self.position
        radius = self.radius
        width = 2
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, position, radius, width)
    
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    