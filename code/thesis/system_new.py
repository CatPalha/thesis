import pygame 
import os
import random
import parameters
from agents import Agent

class App():

    def __init__(self):

        self.width, self.height = parameters.ECOSYSTEM["Width"], parameters.ECOSYSTEM["Height"]
        self.white = (255, 255, 255)
        self.gray = (200,200,200)
        self.black = (0, 0, 0)
        self.fps = 60

        #Where the agent is placed initially
        self.x = random.randrange(50, self.width - 50) 
        self.y = random.randrange(50, self.height - 50) 
        self.speed = parameters.AGENTS["Speed"]
        self.move = [None, None] 
        self.direction = None 

        self.win = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Midge Ecosystem")
        self.clock = pygame.time.Clock()

        self.run, self.loop = True, True

    def draw_window(self):
        """Draw the windows and static agents"""


        self.win.fill(self.white)
        #Place in the window where the midge will be drawn

        cocoa_tree_1 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        cocoa_tree_2 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        cocoa_tree_3 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        cocoa_tree_4 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        cocoa_tree_5 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        cocoa_tree_6 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))

        # water_1 = pygame.image.load(os.path.join("Assets", "water.png"))
        # water_1 = pygame.transform.scale(water_1, (60, 60))

        #Static agents
        self.win.blit(cocoa_tree_1, ((0,0)))
        self.win.blit(cocoa_tree_2, ((300,200)))
        self.win.blit(cocoa_tree_3, ((400,200)))
        self.win.blit(cocoa_tree_4, ((850,550)))
        self.win.blit(cocoa_tree_5, ((750,550)))
        self.win.blit(cocoa_tree_6, ((100,0)))


    def draw_midge(self):
        #Agent transformations: size and rotation
        midge = pygame.image.load(os.path.join("Assets", "midge.png"))
        
        midge_width, midge_height = parameters.AGENTS["Midge Width"], parameters.AGENTS["Midge Heigth"]
        midge = pygame.transform.scale(midge, (midge_width, midge_height))

        self.win.blit(midge, (self.x, self.y))
        

    def draw_mite(self):
        #Agent transformations: size and rotation
        mite = pygame.image.load(os.path.join("Assets", "mite.png"))

        mite_width, mite_height = parameters.AGENTS["Mite Width"], parameters.AGENTS["Mite Heigth"]
        mite = pygame.transform.scale(mite, (mite_width, mite_height))

        self.win.blit(mite, (self.x, self.y))



    def pause_restart(self):
        """Press to space key to pause and restart the game"""

        while self.loop:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.loop = False


    def main(self):

        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                #If the user press X, quit the program
                if event.type == pygame.QUIT: 
                    self.run = False
                
                #If the user press space bar, the program pauses, if presses again the program restarts
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.pause_restart()


            self.draw_window()

            

            pygame.display.update() #update display

        pygame.quit()
    

if __name__ == "__main__":

    app = App()

    midges = []
                    
    for i in range(parameters.AGENTS["Number of midges"]): 
        midge = Agent()
        midges.append(midge)
    
    for midge in midges:

        midge.random_movement()
        midge.borders()
        #midge.draw_agent()

        app.main()



  