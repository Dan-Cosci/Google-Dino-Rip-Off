import os
import pygame as py
import json

import config
from objects import background, button
from main import Game

class Menu():
    def __init__(self):
        py.init

        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((config.SCRWID, config.SCRHEI))
        py.display.set_caption("Dino Game Rip Off")
        py.display.set_icon(py.image.load("assets/standing.png"))

        self.img = py.image.load("assets/start.png").convert_alpha()
        self.bg = background.Background(0,0)

        self.game_score = 0

        self.start = button.Button(config.SCRWID / 2,
                                   config.SCRHEI / 2, 
                                   3.5, 
                                   self.img)

        self.running = True
    
    def score_counter(self):
        if not os.path.exists('src/score.json'):
            print("Creating file object")
            os.mkdir('src')
            with open('src/score.json', 'w') as file:
                score = {'Highscore' : 0}
                json.dump(score, file, indent = 1)


    def draw(self):
        self.bg.draw(self.screen)
        self.bg.update()
        
        self.start.draw(self.screen)
        
        py.display.update()
    
    def action(self):
        self.start.if_click()
        if self.start.clicked:
            self.game = Game(config.SCRWID, config.SCRHEI)
            self.game.game_loop()
            if self.game.run == False:
                self.start.clicked = False
            self.game_score = self.game.score

    def main_menu(self):
        while self.running:
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
            
            print(self.game_score)
            self.score_counter()
            self.draw()
            self.action()


            self.clock.tick(config.FPS)
        


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()