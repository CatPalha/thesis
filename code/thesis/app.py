### RUNS THE SIMULATION ###

import pygame
from menu import *
from agents import Agent
import os
import parameters
import random



class App():

    def __init__(self):

        pygame.init()

        self.run = True
        #self.run, self.pause, self.playing = True, True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.SPACE_KEY = False, False, False, False, False
        self.width, self.height, self.fps = parameters.ECOSYSTEM["Width"], parameters.ECOSYSTEM["Height"], 60
        self.white, self.gray, self.black = (255, 255, 255), (200,200,200), (0, 0, 0)
    
        self.font_name = pygame.font.get_default_font()

        self.display = pygame.Surface(((self.width, self.height)))
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midge Ecosystem")

        self.clock = pygame.time.Clock()
        self.fps = 60


        # self.main_menu = MainMenu(self)
        # self.parameters = ParametersMenu(self)
        # self.rules = RulesMenu(self)
        # self.current_menu = self.main_menu

        self.reset()


    def reset(self):

        self.score = 470
        
        self.x_tree = parameters.ECOSYSTEM["x_tree"]
        self.y_tree = parameters.ECOSYSTEM["y_tree"]

        self.frame_iteration = 0

    
    def draw_agent(self, image_name: str, agent_width: float, agent_height: float, x: float, y: float):
        #Agent transformations: size and rotation
        agent_img = pygame.image.load(os.path.join("Assets", image_name))

        agent = pygame.transform.scale(agent_img, (agent_width, agent_height))
        self.win.blit(agent, (x, y))




    def check_events(self, action):

        self.frame_iteration += 1

        for event in pygame.event.get():

            #Quit the game functionality
            if event.type == pygame.QUIT: 
                #self.run, self.playing = False, False
                self.run = False
                #self.current_menu.menu_running = False

            # #Pause and start functionality
            # if event.type == pygame.KEYDOWN:

            #     if event.key == pygame.K_SPACE:
            #         self.SPACE_KEY = True
            #         self.pause_restart()

            #     if event.key == pygame.K_RETURN:
            #         self.START_KEY = True

            #     if event.key == pygame.K_BACKSPACE:
            #         self.BACK_KEY = True

            #     if event.key == pygame.K_DOWN:
            #         self.DOWN_KEY = True

            #     if event.key == pygame.K_UP:
            #         self.UP_KEY = True
    
        self.move_(action)

        reward = 0

    # def check_events_pause(self):

    #     self.pause = True
        
    #     while self.pause:

    #         for event in pygame.event.get():

    #             if event.type == pygame.QUIT: 
    #                 pygame.quit()
    #                 quit()

    #             if event.type == pygame.KEYDOWN:

    #                 if event.key == pygame.K_SPACE:
        
    #                     self.pause = False

    #                 if event.key == pygame.K_BACKSPACE:
    #                     self.playing = False
    
                    


    def reset_keys(self):

        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.SPACE_K = False, False, False, False, False



    def draw_text(self, text: str, size: int, x_text_pos: float, y_text_pos: float):

        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.black)

        text_rect = text_surface.get_rect()
        text_rect.center = (x_text_pos, y_text_pos)
        self.display.blit(text_surface, text_rect)



    # def pause_restart(self):

    #     self.check_events_pause()




    def move_(self, action):

        directions = {"S":((-1,2), (1,self.speed)), "W":((-self.speed,-1), (-1,2)), "N":((-1,2), (-self.speed,-1)), "E":((1,self.speed), (-1,2))}
        directionsName = ("S", "W",  "N", "E")
        
        #move about once every 5 frames
        if random.randrange(0,5) == 2:
            #if no direction is set, set a random one 
            if self.direction == None:
                self.direction = random.choice(directionsName)
            else:
                #get the index of direction in directions list
                a = directionsName.index(self.direction)
                #set the direction to be the same, or one next to the current direction
                b = random.randrange(a - 1, a + 2)
                #if direction index is outside the list, move back to the start
                if b > len(directionsName) - 1: 
                    b = 0
                self.direction = directionsName[b]

            #change relative x to a random number between min x and max x
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1])
            #change relative y to a random number between min y and max y 
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1])

        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]


    def main_loop(self, midges: list, mites: list):
        #Inside start option, the simulation itself
        self.clock.tick(self.fps)
        self.score = 470

        while self.run:
        #while self.playing:

            self.check_events(self.action)

            # if self.BACK_KEY:
            #     self.playing = False

            # if self.SPACE_KEY:
            #     self.pause_restart()

 
            self.win.fill(self.white)
        
            self.draw_agent("cocoa_tree.png", 133, 135, self.x_tree, self.y_tree)
            #self.draw_agent("water.png", 133, 135, 500, 200)

            for mite in mites:

                mite.random_movement()
                mite.borders()
                self.draw_agent("mite.png", parameters.AGENTS["Mite Width"], parameters.AGENTS["Mite Heigth"], mite.x, mite.y)

            for midge in midges:


                midge.move_()
                midge.borders()

                self.draw_agent("midge.png", parameters.AGENTS["Midge Width"], parameters.AGENTS["Midge Heigth"], midge.x, midge.y)


                if midge.x == self.x_tree and midge.y == self.y_tree:
                    self.score += 1

                if midge.x <= -10 or midge.x >= self.width + 10:
                    self.score -= 1

                
                if midge.x == mite.x and midge.y == mite.y:
                    self.score -= 1

                if self.score == 0:
                    self.run = False
                    #self.playing = False
                    self.reset_keys()
    
  

            print("Midge Score: ", self.score)


            pygame.display.update()
            self.reset_keys()







  

