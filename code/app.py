### RUNS THE SIMULATION ###

import pygame
from menu import MainMenu
from agents import Agent
import os

#agent = Agent()

class App():

    def __init__(self):

        pygame.init()
        self.run, self.loop, self.playing = True, False, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.width, self.height, self.fps = 1000, 800, 60
        self.white, self.gray, self.black = (255, 255, 255), (200,200,200), (0, 0, 0)
        #self.font_name = 'ARIAL'
        self.font_name = pygame.font.get_default_font()

        self.display = pygame.Surface(((self.width, self.height)))
        self.win = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.current_menu = MainMenu(self)

    
    def draw_agent(self, image_name: str, agent_width: float, agent_height: float, x: float, y: float):
        #Agent transformations: size and rotation
        agent_img = pygame.image.load(os.path.join("Assets", image_name))

        agent = pygame.transform.scale(agent_img, (agent_width, agent_height))
        self.win.blit(agent, (x, y))


    def check_events(self):

        for event in pygame.event.get():

            #Quit the game functionality
            if event.type == pygame.QUIT: 
                self.run, self.playing = False, False
                self.current_menu.window = False

            #Pause and start functionality
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.loop = False

                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            

    def reset_keys(self):

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def draw_text(self, text: str, size: int, x_text_pos: float, y_text_pos: float):

        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.black)
        text_rect = text_surface.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        self.display.blit(text_surface, text_rect)


    def main_loop(self):
        #Inside start option, the simulation itself
        
        while self.playing:
            self.check_events()

            if self.START_KEY:
                self.playing = False

            self.win.fill(self.white)
            pygame.display.set_caption("Midge Ecosystem")

            #Static agents, like trees and water
            self.draw_agent("cocoa_tree.png", 133, 135, 300, 200)
            self.draw_agent("cocoa_tree.png", 133, 135, 500, 200)
            self.draw_agent("water.png", 100, 80, 425, 300)

            for midge in midges:

                midge.random_movement()
                midge.borders()
                self.draw_agent("midge.png", 350, 150, midge.x, midge.y)

            for mite in mites:

                mite.random_movement()
                mite.borders()
                self.draw_agent("mite.png", 400, 200, mite.x, mite.y)


            pygame.display.update()
            self.reset_keys()


midges = []

for i in range(3): 
    midge = Agent()
    midges.append(midge)


mites = []

for i in range(3): 
    mite = Agent()
    mites.append(mite)




    # def to_run(self):

    #     while self.run:
            
    #         self.clock.tick(self.fps)
    #         #self.check_events()
    #         self.main_loop()
    #         self.win.fill(self.white)
    #         pygame.display.set_caption("Midge Ecosystem")

    #         self.draw_agent("cocoa_tree.png", 133, 135, 300, 200)
    #         self.draw_agent("cocoa_tree.png", 133, 135, 500, 200)
    #         self.draw_agent("water.png", 100, 80, 425, 300)

    #         for midge in midges:

    #             midge.random_movement()
    #             midge.borders()
    #             self.draw_agent("midge.png", 350, 150, midge.x, midge.y)

    #         for mite in mites:

    #             mite.random_movement()
    #             mite.borders()
    #             self.draw_agent("mite.png", 400, 200, mite.x, mite.y)

            
    #         pygame.display.update()
    #         self.reset_keys()

    # print("How many midges?")



# print("How many trees?")

# midge_number = int(input())

