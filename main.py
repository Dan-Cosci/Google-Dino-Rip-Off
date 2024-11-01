import pygame as py
import config

from objects import background, obstacles, player

class Game():
    def __init__(self,scrwid, scrhei):
        py.init()
        self.clock = py.time.Clock()
        self.screen = py.display.set_mode((scrwid, scrhei))
        py.display.set_caption("Mini game")
        py.display.set_icon(py.image.load("assets/frame_1.png"))
        
        self.background = background.Background(0,0)

        self.player = player.Player(100,240)
        self.obstacle = obstacles.Obstacles()

        self.run = True


    def draw(self):
        self.screen.fill("violet")

        self.background.draw(self.screen)
        self.background.update()

        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        
        py.display.update()
        self.clock.tick(config.FPS)

    def game_loop(self):
        while self.run:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.run = False
            self.player.movement()        
            self.draw()

        py.quit()     

if __name__ == "__main__":
    game = Game(config.SCRWID,config.SCRHEI)
    game.game_loop()