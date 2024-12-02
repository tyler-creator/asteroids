import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        velocity = pygame.Vector2(0,0)
        position = pygame.Vector2(x,y)
        self.rotation = 0
        super().__init__(position, velocity, radius)        

    def draw(self, screen):
        position = self.position
        radius = self.radius
        width = 2
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, position, radius, width)
    
    
    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        random_angle = random.uniform(20,50)
        asteroid1.velocity = self.velocity.rotate(random_angle)* 1.2
        asteroid2.velocity = self.velocity.rotate(-random_angle)* 1.2
        return asteroid1, asteroid2
            
        
        

    