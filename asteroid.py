import pygame
from circleshape import CircleShape
from constants import *
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
            return
        else:
            new_angle = random.uniform(20, 50)
            split_1 = self.velocity.rotate( new_angle)
            split_2 = self.velocity.rotate(new_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_s1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_s2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_s1.velocity = split_1 * 1.2
            asteroid_s2.velocity = split_2 * 1.2