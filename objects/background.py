import pygame as py

class Background(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)

        self.bg_speed = 1
        self. gr_speed = 3

        self.bg = py.image.load("assets/background.png").convert_alpha()
        self.bg = py.transform.scale_by(self.bg, 6)  
        self.bg_rect = self.bg.get_rect(topleft = (x,y))

        self.ground = py.image.load("assets/ground.png").convert_alpha()
        self.gr_rect = self.ground.get_rect(bottomleft = (x,y + 460))

    def draw(self, screen):
        screen.blit(self.bg, self.bg_rect)
        screen.blit(self.bg, (self.bg_rect.x + self.bg.get_width(), self.bg_rect.y))

        screen.blit(self.ground, self.gr_rect)
        screen.blit(self.ground, (self.gr_rect.x + self.ground.get_width(), self.gr_rect.y))
    
    def update(self):
        self.gr_rect.x -= self.gr_speed
        if self.gr_rect.x <= -int(self.ground.get_width()):
            self.gr_rect.x = 0
        
        self.bg_rect.x -= self.bg_speed
        if self.bg_rect.x <= -int(self.bg.get_width()):
            self.bg_rect.x = 0
        