import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # Subclass must override
        pass


    def update(self, dt):
        # Subclass must override
        pass


    def collisionCheck(self, collider) -> bool:
        distance = self.position.distance_to(collider.position)
        if distance < self.radius + collider.radius:
            return True
        else:
            return False