import pygame 
import Player as P 
import Rocket as R
import config as cfg 
import TestObject as TO


class Game:

    def __init__(self, player="human"):
        self.rocket = R.Rocket()
        self.win = pygame.display.set_mode((cfg.WIN_WIDTH, cfg.WIN_HEIGHT))
        self.player = player    # Build the AI around here 
        self.to = TO.TestObject() 
        floor_x, floor_y = cfg.translate_coords(-10, 0)
        self.floor = (floor_x, floor_y, cfg.WIN_WIDTH, cfg.WIN_HEIGHT)


    def run(self):
        clock = pygame.time.Clock()
        alive = True
        self.render_window()
        while alive:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    alive = False
                
            self.update(keys)
            self.render_window()
            clock.tick(cfg.FPS)


    def update(self, keys):
        self.rocket.move(keys)
        self.to.update(keys)


    def render_window(self):
        self.win.fill((200, 200, 0))
        self.rocket.draw(self.win)
        pygame.draw.rect(self.win, (0, 0, 0), self.floor)

        self.to.draw(self.win)

        pygame.draw.circle(self.win, (255, 255, 255), cfg.translate_coords(0, 0), 2)

        pygame.display.flip()