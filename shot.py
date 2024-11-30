import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED

class Shot(CircleShape):
    SHOT_RADIUS = 5
    containers = None
    
    def __init__(self, x, y):
        position = pygame.Vector2(x,y)
        velocity = pygame.Vector2(0, 0)
        super().__init__(position, velocity, self.SHOT_RADIUS)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt