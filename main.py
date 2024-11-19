# why do I need to comment this shit

# Imports from python stdlib
import os
import pygame as py
import json

# Lib created for game
import config
from objects import background, button
from game import Game


# Main menu function
class Menu():

    # Initilization function
    def __init__(self):
        py.init()                                                           # Init the pygame module
        
        # Loads pygame basic parameters
        py.mixer.init()                                                     # pygame mixer
        self.clock = py.time.Clock()                                        # FPS    
        self.screen = py.display.set_mode((config.SCRWID, config.SCRHEI))   # Main window
        py.display.set_caption("Dino Game Rip Off")                         # Window caption
        py.display.set_icon(py.image.load("assets/icon.png"))               # Window  Icon

        # images
        self.img = py.image.load("assets/start.png").convert_alpha()        # Load start.png
        self.bg = background.Background(0,0)                                # Generates moving bg

        # Background music
        py.mixer.music.load('assets/game_music.mp3')                        # Loads music
        py.mixer.music.play(-1)                                             # Plays music in a loop

        # Loading font for text
        self.title = py.font.Font('assets/dogica.ttf', 40)
        self.title_2 = py.font.Font('assets/dogica.ttf', 15)

        # Score tracker
        self.game_score = 0
        self.cur_high = self.get_high()

        # button sprite init
        self.start = button.Button(config.SCRWID / 2,
                                   config.SCRHEI / 2, 
                                   3.5, 
                                   self.img)

        # run condition
        self.running = True
    

    # File checker function
    def file_check(self):
        
        # If file is Null | generates directory and JSON
        if not os.path.exists('src/score.json'):
            print("Creating file object")
            os.mkdir('src')
            with open('src/score.json', 'w') as file:
                score = {'Highscore' : 0}
                json.dump(score, file, indent = 1)


    # Return the current highscore
    def get_high(self):
        
        # Check if file exists
        self.file_check()

        # Open files and returns the int highscore
        with open('src/score.json', 'r') as file:
            data = json.load(file)

        return data['Highscore']


    # checks if score is greater than highscore
    def score_check(self):
        
        # Open and read file for data gathering
        with open('src/score.json', 'r') as file:           
            data = json.load(file)

        # Checks if score is  greater than the highscore
        if data['Highscore'] < self.game_score:             
            data['Highscore'] = self.game_score
            
            # Rewrites data
            with open('src/score.json', 'w') as file_2:    
                json.dump(data, file_2, indent= 2)


    # Draw text function
    def draw_text(self, screen):
        
        # Title text
        title1 = self.title.render("Pixel Runner",False,"Black")
        pos1 = title1.get_rect(center = (config.SCRWID / 2, config.SCRHEI / 2  - 100))
        
        # Displays current highscore
        if self.cur_high < self.game_score:
            self.cur_high = self.game_score

        # Title text
        title2 = self.title_2.render(f"Highscore:{str(self.cur_high)}" ,False,"Black")
        pos2 = title2.get_rect(center = (config.SCRWID / 2, config.SCRHEI / 2  - 50))
        
        # Draw text to screen
        screen.blit(title2,pos2)
        screen.blit(title1,pos1)


    # Main draw function
    def draw(self):
        
        # Draws and updates the background
        self.bg.draw(self.screen)
        self.bg.update()
        
        # draw text
        self.draw_text(self.screen)
        self.start.draw(self.screen)
        
        # updates the current window
        py.display.update()
    

    # Detect functions
    def action(self):
        self.start.if_click()
        if self.start.clicked:
            self.game = Game(config.SCRWID, config.SCRHEI)
            self.game.game_loop()
            if self.game.run == False:
                self.start.clicked = False
            self.game_score = self.game.score
            self.cur_high = self.get_high()


    # Main menu loop
    def main_menu(self):
        
        self.file_check()                       # Final check if file exists
 
        while self.running:                     # Looping
            
            for event in py.event.get():        # Checks if the program is closed
                if event.type == py.QUIT:
                    self.running = False
                    py.quit()
            
            self.draw()                         # draw to the screen
            self.action()                       # check for action
            self.score_check()                  # check score


            self.clock.tick(config.FPS)         # FPS
        


if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()