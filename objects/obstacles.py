import pygame as py
import config

class Fly(py.sprite.Sprite):
    def __init__(self,x, y):
        py.sprite.Sprite.__init__(self)
        self.fly_img = [
            py.image.load("assets/fly_1.png").convert_alpha(),
            py.image.load("assets/fly_3.png").convert_alpha()
        ]
        self.img_index = 0
        self.counter = 0

        self.current_img = py.transform.scale_by(self.fly_img[self.img_index], 3.5)
        self.img_rect = self.current_img.get_rect(midbottom = (x,y))
    
    
    def draw(self, screen):
        self.counter += 1
        cooldown = 7 
        if self.counter > cooldown:
                self.counter = 0
                self.img_index += 1
                if self.img_index >= len(self.fly_img):
                    self.img_index = 0

        self.current_img = py.transform.scale_by(self.fly_img[self.img_index], 3.5)
        screen.blit(self.current_img, self.img_rect)
        
        # py.draw.rect(screen, 'red', self.img_rect)
