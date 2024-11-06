import pygame as py
import random as rand

import config
from objects import background, obstacles, player

class Game():
    def __init__(self,scrwid, scrhei):
        py.init()

        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((scrwid, scrhei))
        py.display.set_caption("Dino Game Rip Off")
        py.display.set_icon(py.image.load("assets/frame_1.png"))
        
        self.background = background.Background(0,0)

        self.player = player.Player(100,293)
        self.start_pos = self.player.img_rect

        self.run = True
        self.score = 0        
        self.passed_1 = False

        self.obstacle_list_1 = []
        self.obstacle_timer = py.USEREVENT + 1
        py.time.set_timer(self.obstacle_timer, 700)


    def reset_game(self):
        self.obstacle_list_1.clear()
        self.player.img_rect.midbottom = [100, 293]


    def obstacle_gen(self):
        choice_1 = 0 # rand.randint(0,1)
        if choice_1 == 0:
            self.obstacle_list_1.append(obstacles.Fly(rand.randint(750,1000), rand.randint(150 ,290)))
        
    def obstacle_loop(self):
        
        for obj in self.obstacle_list_1:
            obj.img_rect.x  -= 9
            obj.draw(self.screen)
            if obj.img_rect.x <= - 100:
                self.obstacle_list_1.pop(0)

            if self.player.img_rect.left  > obj.img_rect.left\
                and self.player.img_rect.right < obj.img_rect.right\
                and self.passed_1 == False:
                self.passed_1 = True
            if self.passed_1 == True:    
                if self.player.img_rect.left  > obj.img_rect.right:
                    self.score += 1
                    print(self.score)
                    self.passed_1 = False

            if self.player.img_rect.colliderect(obj.img_rect):
                self.reset_game()
                self.run = False


    def draw(self):
        self.screen.fill("violet")

        self.background.draw(self.screen)
        self.background.update()

        self.obstacle_loop()

        self.player.draw(self.screen)
        py.display.update()
        self.clock.tick(config.FPS)


    def game_loop(self):
        while self.run:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.run = False
                if event.type == self.obstacle_timer:
                    self.obstacle_gen()

            self.player.movement()        
            self.draw()
        return self.score

if __name__ == "__main__":
    game = Game(config.SCRWID,config.SCRHEI)
    game.game_loop()