import pygame
import config as cfg
from config import dt


class TestObject:
    width = 10
    height = 20 
    # Müssen die noch irgendwe durch den Menschen oder den AI kontrollierbar machen 

    def __init__(self):
        self.x = 0
        self.y = 10
        self.x_vel = 0
        self.y_vel = 0
        self.surface = pygame.Surface((20, 20))
        self.surface.set_colorkey((0, 0, 0))
        self.rect = self.surface.get_rect(center=(100, 100))
        self.angle = 0

    def update(self, keys):
        if keys[pygame.K_d]:
            self.angle += 10*dt
        if keys[pygame.K_a]:
            self.angle -= 10*dt
        

    def draw(self, win): 
        self.angle = (self.angle + 10*dt) % 360
        image = pygame.transform.rotate(self.surface, self.angle)
        self.rect = image.get_rect()

        self.rect.y += 1.5

        pygame.draw.rect(self.surface, (100, 100, 100), (0, 0, 20, 20), )
        win.blit(image, self.rect)

        x, y = cfg.translate_coords(self.x, self.y)
        self.rect = (int(x - self.width/2), y - self.height, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.rect)
        