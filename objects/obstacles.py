import pygame as py
import config

class Obstacles(py.sprite.Sprite):
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.fly_img = [
            py.image.load("assets/fly_1.png").convert_alpha(),
            py.image.load("assets/fly_3.png").convert_alpha()
        ]
        self.img_index = 0
        self.counter = 0

        self.x = config.SCRWID

        self.obstacle = py.image.load("assets/ground_obstacle.png").convert_alpha()
    
    
    def draw(self, screen):
        self.counter += 1
        cooldown = 7 
        if self.counter > cooldown:
                self.counter = 0
                self.img_index += 1
                if self.img_index >= len(self.fly_img):
                    self.img_index = 0

        self.current_img = py.transform.scale_by(self.fly_img[self.img_index], 3.5)
        screen.blit(self.current_img, (self.x,100))
        self.x -= 3
        if self.x <= -1 * self.current_img.get_width():
            self.x = config.SCRWID