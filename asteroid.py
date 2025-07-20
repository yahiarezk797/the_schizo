from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 0
        else:
            angle = random.uniform(20, 50)
            d1 = self.velocity.rotate(angle)
            d2 = self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_r)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_r)
            asteroid1.velocity = d1
            asteroid2.velocity = d2
            