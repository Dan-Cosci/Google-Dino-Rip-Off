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

        self.run = True

        self.obstacle_list_1 = []
        self.obstacle_list_2 = []
        self.obstacle_timer = py.USEREVENT + 1
        py.time.set_timer(self.obstacle_timer, 1200)


    def obstacle_gen(self):
        choice_1 = rand.randint(0,1)
        if choice_1 == 0:
            self.obstacle_list_1.append(obstacles.Fly(rand.randint(750,900), rand.randint(100 ,200)))
        
        choice_2 = rand.randint(0,1)
        if choice_2 == 0:
            self.obstacle_list_2.append(obstacles.Box(rand.randint(750,950), 295))


    def obstacle_loop(self):
        for obj in self.obstacle_list_1:
            obj.img_rect.x  -= 5
            obj.draw(self.screen)
            if obj.img_rect.x <= - 100:
                self.obstacle_list_1.pop(0)
        
        for obj in self.obstacle_list_2:
            obj.img_rect.x  -= 3
            obj.draw(self.screen)
            if obj.img_rect.x <= - 100:
                self.obstacle_list_2.pop(0)        
        

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

        py.quit()     

if __name__ == "__main__":
    game = Game(config.SCRWID,config.SCRHEI)
    game.game_loop()