import pygame as py
import config

class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        
        self.image = [
            py.image.load("assets/frame_1.png").convert_alpha(),
            py.image.load("assets/frame_2.png").convert_alpha()
        ]
        self.img_jump = [
            py.image.load("assets/jump_1.png").convert_alpha(),
            py.image.load("assets/jump_2.png").convert_alpha()
        ]
        self.img_index = 0
        self.counter = 0

        self.current_img = self.image[self.img_index]        
        self.img_rect = self.current_img.get_rect(midbottom = (x,y))
        self.ground = self.img_rect.y

        self.is_jump = False
        self.jumpcount = 10

        self.gravity_index = 0.2
        self.grav = 0

    
    def draw(self,screen):
        if not self.is_jump:    
            self.counter += 1
            cooldown = 9
            if self.counter > cooldown:
                self.counter = 0
                self.img_index += 1
                if self.img_index >= len(self.image):
                    self.img_index = 0

            self.current_img = self.image[self.img_index]
        else:
            self.counter += 1
            cooldown = 5
            if self.counter > cooldown:
                self.counter = 0
                self.img_index += 1
                if self.img_index >= len(self.img_jump):
                    self.img_index = 0

            self.current_img = self.img_jump[self.img_index]

        self.current_img = py.transform.scale_by(self.current_img, 3.5)
        screen.blit(self.current_img, self.img_rect)


    def movement(self):
        self.keys = py.key.get_pressed()
        if self.keys[py.K_LEFT]:
            if self.img_rect.x > 0:
                self.img_rect.x -=5

        if self.keys[py.K_RIGHT]:
            if self.img_rect.x < (config.SCRWID - self.current_img.get_width()):
                self.img_rect.x +=5
        
        if not self.is_jump:    
            if self.keys[py.K_UP]:
                self.is_jump = True
        else:
            if self.jumpcount >= -10:
                neg = 1
                if self.jumpcount < 0:
                    neg = -1
                self.img_rect.y -= (self.jumpcount ** 2) * 0.2 * neg
                self.jumpcount -= 0.6
            else:
                self.jumpcount = 10
                self.is_jump = False
                self.img_rect.y = self.ground        
