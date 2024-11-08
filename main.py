import os
import pygame as py
import json

import config
from objects import background, button
from game import Game

class Menu():
    def __init__(self):
        py.init()

        py.mixer.init()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((config.SCRWID, config.SCRHEI))
        py.display.set_caption("Dino Game Rip Off")
        py.display.set_icon(py.image.load("assets/standing.png"))

        self.img = py.image.load("assets/start.png").convert_alpha()
        self.bg = background.Background(0,0)

        py.mixer.music.load('assets/game_music.mp3')
        py.mixer.music.play(-1)

        self.title = py.font.Font('assets/dogica.ttf', 40)
        self.title_2 = py.font.Font('assets/dogica.ttf', 15)

        self.game_score = 0
        self.cur_high = self.get_high()

        self.start = button.Button(config.SCRWID / 2,
                                   config.SCRHEI / 2, 
                                   3.5, 
                                   self.img)

        self.running = True
    
    def file_check(self):
        if not os.path.exists('src/score.json'):
            print("Creating file object")
            os.mkdir('src')
            with open('src/score.json', 'w') as file:
                score = {'Highscore' : 0}
                json.dump(score, file, indent = 1)


    def get_high(self):
        
        self.file_check()

        with open('src/score.json', 'r') as file:
            data = json.load(file)
        return data['Highscore']


    def score_check(self):
        with open('src/score.json', 'r') as file:
            data = json.load(file)
        if data['Highscore'] < self.game_score:
            data['Highscore'] = self.game_score
            with open('src/score.json', 'w') as file_2:
                json.dump(data, file_2, indent= 2)

    def draw_text(self, screen):
        title1 = self.title.render("Pixel Runner",False,"Black")
        pos1 = title1.get_rect(center = (config.SCRWID / 2, config.SCRHEI / 2  - 100))
        
        if self.cur_high < self.game_score:
            self.cur_high = self.game_score

        title2 = self.title_2.render(f"Highscore:{str(self.cur_high)}" ,False,"Black")
        pos2 = title2.get_rect(center = (config.SCRWID / 2, config.SCRHEI / 2  - 50))
        
        screen.blit(title2,pos2)
        screen.blit(title1,pos1)

    def draw(self):
        self.bg.draw(self.screen)
        self.bg.update()
        
        self.draw_text(self.screen)
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
            self.cur_high = self.get_high()

    def main_menu(self):
        self.file_check()

        while self.running:
            
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
            
            self.draw()
            self.action()
            self.score_check()


            self.clock.tick(config.FPS)
        


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()