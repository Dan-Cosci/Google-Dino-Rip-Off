import pygame as py




class Button(py.sprite.Sprite):
    def __init__(self, x,y, scale, image):
        py.sprite.Sprite.__init__(self)
        self.img = image
        self.img = py.transform.scale_by(self.img, scale)
        self.img_rect = self.img.get_rect(center = (x,y))

        self.clicked = False

    def if_click(self):
        pos = py.mouse.get_pos()
        if self.img_rect.collidepoint(pos):
            if py.mouse.get_pressed()[0] ==  1:
                print("clicked")
                self.clicked = True
        
    def click(self):
        return self.clicked

    def draw(self, screen):
        screen.blit(self.img, self.img_rect)