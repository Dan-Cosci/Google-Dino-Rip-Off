import pygame as py

class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        
        self.image = [
            py.image.load("assets/frame_1.png").convert_alpha(),
            py.image.load("assets/frame_2.png").convert_alpha()
        ]
        self.img_index = 0
        self.counter = 0

        self.current_img = self.image[self.img_index]        
        self.img_rect = self.current_img.get_rect(midbottom = (x,y))

        self.gravity_index = 0.2
        self.grav = 0

    
    def draw(self,screen):
        self.counter += 1
        cooldown = 9
        if self.counter > cooldown:
            self.counter = 0
            self.img_index += 1
            if self.img_index >= len(self.image):
                self.img_index = 0

        self.current_img = self.image[self.img_index]
        self.current_img = py.transform.scale_by(self.current_img, 3.5)
        screen.blit(self.current_img, self.img_rect)

    def gravity(self):
        if self.img_rect.y < 222:
            self.grav += self.gravity_index 
            self.img_rect.y += self.grav
        else:
            self.grav = 0
            self.img_rect.y = 222

    def movement(self):
        self.keys = py.key.get_pressed()
        if self.keys[py.K_LEFT]:
            self.img_rect.x -=5
        if self.keys[py.K_RIGHT]:
            self.img_rect.x +=5
        if self.keys[py.K_UP]:
            self.img_rect.y -= 10
        if self.keys[py.K_DOWN]:
            if self.img_rect.y < 222:
                self.img_rect.y += 5          
