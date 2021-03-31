### RUNS THE SIMULATION ###

import pygame
from menu import *
from agents import Agent
import os

class App():

    def __init__(self):

        pygame.init()
        self.run, self.pause, self.playing = True, True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.SPACE_KEY = False, False, False, False, False
        self.width, self.height, self.fps = 1500, 1000, 60
        self.white, self.gray, self.black = (255, 255, 255), (200,200,200), (0, 0, 0)
    
        self.font_name = pygame.font.get_default_font()
        self.input_font = pygame.font.Font(self.font_name, 32)
        self.user_input = "Teste"
        self.input_surface = self.input_font.render(self.user_input, True, self.black)
        self.input_pos = (0, 10)

        self.display = pygame.Surface(((self.width, self.height)))
        self.win = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.main_menu = MainMenu(self)
        self.parameters = ParametersMenu(self)
        self.rules = RulesMenu(self)
        self.current_menu = self.main_menu



    
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
                self.current_menu.menu_running = False

            #Pause and start functionality
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                    self.pause_restart()

                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    
    def check_events_pause(self):

        self.pause = True
        
        while self.pause:

            for event in pygame.event.get():

                if event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
        
                        self.pause = False
                    
                    if event.key == pygame.K_BACKSPACE:
                        #TODO
                        pass
    
                    


    def reset_keys(self):

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.SPACE_K = False, False, False, False, False


    def draw_text(self, text: str, size: int, x_text_pos: float, y_text_pos: float):

        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.black)

        text_rect = text_surface.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        self.display.blit(text_surface, text_rect)



    def pause_restart(self):

        self.check_events_pause()



    def main_loop(self, midges: list, mites: list):
        #Inside start option, the simulation itself
        self.clock.tick(self.fps)

        while self.playing:

            self.check_events()

            if self.BACK_KEY:
                self.playing = False

            # if self.SPACE_KEY:
            #     self.pause_restart()

           
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





  

