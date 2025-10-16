import pygame
import random
from src.components.circleshape import CircleShape
from src.utils.constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self,  dt):
        self.position += self.velocity * dt
        
    def split(self):
        current_pos = self.position
        old_radius = self.radius
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)
        
        asteroid_one = Asteroid(current_pos.x, current_pos.y, new_radius)
        asteroid_two = Asteroid(current_pos.x, current_pos.y, new_radius)

        asteroid_one.velocity = v1 * 1.2
        asteroid_two.velocity = v2 * 1.2