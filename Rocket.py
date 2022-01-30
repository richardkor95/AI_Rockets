import pygame
import config as cfg 
from config import dt


class Rocket:
    width = 10
    height = 20 
    # Müssen die noch irgendwe durch den Menschen oder den AI kontrollierbar machen 

    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0


    def move(self, keys):
        self.y_vel -= cfg.ACC*dt
        self.y += self.y_vel*dt
        self.x_vel -= self.x_vel*0.5*dt
        self.x += self.x_vel
        
        if self.y <= 0:
            self.y = 0
            self.y_vel = 0

        if keys[pygame.K_UP]:
            self.y_vel += 2*cfg.ACC*dt
            print('oresses')
        if keys[pygame.K_LEFT]:
            self.x_vel -= 0.1*dt
        if keys[pygame.K_RIGHT]:
            self.x_vel += 0.1*dt


    def draw(self, win): 
        x, y = cfg.translate_coords(self.x, self.y)
        self.rect = (int(x - self.width/2), y - self.height, self.width, self.height)
        pygame.draw.rect(win, (255, 0, 0), self.rect)
        