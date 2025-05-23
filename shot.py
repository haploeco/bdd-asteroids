import pygame

from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt
