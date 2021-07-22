#Import necessary packages
import pygame
import parameters
import os
import random
from agents import Mite, Midge
from gym import Env
from gym.spaces import Discrete



class App(Env):

    def __init__(self):

        self.width, self.height = parameters.ECOSYSTEM["Width"], parameters.ECOSYSTEM["Height"]
        self.white = (255, 255, 255)
        self.fps = 15
        self.clock = pygame.time.Clock() 


        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midge Ecosystem")

        self.run = True
        self.score = 470
        self.reward = 0

        self.action_space = Discrete(5)
        self.observation_space = Discrete(6)

        #A midge can life until 691200 seconds
        self.life_span = 691200
        self.temperature = round(random.uniform(20, 26), 2)
   

    def draw_window(self):
        """Draw the windows and static agents"""


        self.win.fill(self.white)

        cocoa_tree = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        
        water = pygame.image.load(os.path.join("Assets", "water.png"))
        water = pygame.transform.scale(water, (60, 60))

        self.win.blit(cocoa_tree, ((parameters.ECOSYSTEM["x_tree_1"], parameters.ECOSYSTEM["y_tree_1"])))
        self.win.blit(cocoa_tree, ((parameters.ECOSYSTEM["x_tree_2"], parameters.ECOSYSTEM["y_tree_2"])))
        self.win.blit(water, (parameters.ECOSYSTEM["x_water"], parameters.ECOSYSTEM["y_water"]))

    
    def step(self, action, midges: list, mites: list):
        self.state += action -1
        self.life_span -= 1

        ## REWARDS AND SCORE
        ##FOOD
        for midge in midges:
            if 340 <= midge.x <= 400:
                if 142 <= midge.y == 447:
                    self.score += 1
                    self.reward += 1

            if 39 <= midge.x <= 97:
                if 150 <= midge.y <= 155:
                    self.score += 1
                    self.reward += 1
        
            ## RESTING PLACE
            if 82 <= midge.x <= 101:
                if 180 <= midge.y <= 185:
                    self.score += 0.5
                    self.reward += 0.5 

            ## END OF THE GAME
            if self.score <= 0:
                self.reward -= 2
                print("GAME OVER")
                self.run = False

            if self.score > 470:
                self.score = 470
            
            #If it's survives gains a reward
            #In each iteration it loses score, bc it loses energy
            if self.score > 0:
                self.score -= 0.01
                self.reward += 0.01

            ## PREDATORS
            for mite in mites:

                if mite.x - 4 <= midge.x <= mite.x + 4:
                    if mite.y - 4 <= midge.y <= mite.y + 4:
                        self.score -= 10
                        self.reward -= 1

        if self.life_span:
            done = True
        else:
            done = False

        #self.state += random.randint(-1, 1)

        info = {}

        return self.state, reward, done, info

        def reset(self):

            self.life_span = 691200



    def main(self, midges, mites):
     
        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                #If the user press X, quit the program
                if event.type == pygame.QUIT: 
                    self.run = False


            self.draw_window()

            for mite in mites:

                mite.movement()
                mite.borders()
                mite.draw_mite()

            for i, midge in enumerate(midges):
                midge.movement()
        
            
                midge.borders()
                midge.draw_midge()



                print("Score: ", self.score, " Reward: ", self.reward)
                print("Midge x: ", midge.x, "Midge y", midge.y)       


            pygame.display.update() 
        pygame.quit()


#This guarantees the function main only runs when this files runs, if I want to run from somewhere else I need to delete this
if __name__ == "__main__":

    app = App()

    mites = []

    for i in range(parameters.AGENTS["Number of predators"]): 
        mite = Mite(app)
        mites.append(mite)
    

    midges = [] 

    for i in range(parameters.AGENTS["Number of midges"]): 
        midge = Midge(app)
        midges.append(midge)
    
    app.main(midges, mites)
    


