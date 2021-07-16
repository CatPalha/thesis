#Import necessary packages
import random
import pygame
import os
import parameters



class App:

    def __init__(self):

        self.width, self.height = parameters.ECOSYSTEM["Width"], parameters.ECOSYSTEM["Height"]
        self.white = (255, 255, 255)
        #self.black = (0, 0, 0)
        self.fps = 60
        self.clock = pygame.time.Clock() 


        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midge Ecosystem")

        self.run = True
        self.score = parameters.ECOSYSTEM["Initial score"]
        self.reward = 0
   

    def draw_window(self):
        """Draw the windows and static agents"""

        self.win.fill(self.white)

        cocoa_tree = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
        
        water = pygame.image.load(os.path.join("Assets", "water.png"))
        water = pygame.transform.scale(water, (60, 60))

        self.win.blit(cocoa_tree, ((parameters.ECOSYSTEM["x_tree_1"], parameters.ECOSYSTEM["y_tree_1"])))
        self.win.blit(cocoa_tree, ((parameters.ECOSYSTEM["x_tree_2"], parameters.ECOSYSTEM["y_tree_2"])))
        self.win.blit(water, (parameters.ECOSYSTEM["x_water"], parameters.ECOSYSTEM["y_water"]))

    

    def main(self, midges, mites):
     
        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                #If the user pressi X, quit the program
                if event.type == pygame.QUIT: 
                    self.run = False


            self.draw_window()

            for mite in mites:

                mite.movement()
                mite.borders()
                mite.draw_mite()

            for midge in midges: 
                midge.movement()
                midge.borders()
                midge.draw_midge()

                ## REWARDS AND SCORE
                if (midge.x == parameters.ECOSYSTEM["x_tree_1"] and midge.y == parameters.ECOSYSTEM["y_tree_1"]) or (midge.x == parameters.ECOSYSTEM["x_tree_2"] and midge.y == parameters.ECOSYSTEM["y_tree_2"]):
                    self.score += 20
                    self.reward += 1

                if midge.x < -108 or midge.x > self.width:
                    self.score -= 5
                    self.reward -= 1

                if midge.x == mite.x and midge.y == mite.y:
                    self.score -= -20
                    self.reward -= 1

                if self.score == 0:
                    self.reward -= 1
                    self.run = False

            print("Score: ", self.score, " Reward: ", self.reward)
            print("Midge x: ", midge.x, "Midge y", midge.y)

            

            #self.reward(midge, mite)

            pygame.display.update() 
        pygame.quit()


class Midge:

    def __init__(self, app):

        self.app = app
        self.x = random.randrange(200, parameters.ECOSYSTEM["Width"] - 200) 
        self.y = random.randrange(200, parameters.ECOSYSTEM["Height"] - 200) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None 

    def draw_midge(self):
      
        midge = pygame.image.load(os.path.join("Assets", "midge.png"))
        
        midge = pygame.transform.scale(midge, (parameters.AGENTS["Midge Width"], parameters.AGENTS["Midge Height"]))

        app.win.blit(midge, (self.x, self.y))
    
        
    def movement(self):

        directions = {"SW":((-self.speed,-1), (1,self.speed)), "NW":((-self.speed,-1), (-self.speed,-1)), "NE":((1,self.speed), (-self.speed,-1)), "SE":((1,self.speed), (1,self.speed))}

        directionsName = ("SW",  "NW", "NE",  "SE") 
        
        #move about once every 5 frames
        if random.randrange(0,5) == 2:
            #if no direction is set, set a random one 
            if self.direction == None:
                self.direction = random.choice(directionsName)
            else:
                #get the index of direction in directions list
                a = directionsName.index(self.direction)
                #set the direction to be the same, or one next to the current direction
                b = random.randrange(a - 1,a + 2)
                #if direction index is outside the list, move back to the start
                if b > len(directionsName) - 1: 
                    b = 0
                self.direction = directionsName[b]

            #change relative x to a random number between min x and max x
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1])
            #change relative y to a random number between min y and max y 
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1])

        
            smallOffset = random.random() 
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]

    def borders(self):
        """Ensures that the world is round"""

        if self.y < 0:
            self.y = app.height

        if self.y > app.height:
            self.y = 0
    

class Mite:

    def __init__(self, app):

        self.app = app
        self.x = random.randrange(200, parameters.ECOSYSTEM["Width"] - 200) 
        self.y = random.randrange(200, parameters.ECOSYSTEM["Height"] - 200) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None 
    
        
    def draw_mite(self):
        
        mite = pygame.image.load(os.path.join("Assets", "mite.png"))

        mite = pygame.transform.scale(mite, (parameters.AGENTS["Mite Width"], parameters.AGENTS["Mite Height"]))

        app.win.blit(mite, (self.x, self.y))
        

    def movement(self):

        directions = {"S":((-1,2), (1,self.speed)), "SW":((-self.speed,-1), (1,self.speed)), "W":((-self.speed,-1), (-1,2)), "NW":((-self.speed,-1), (-self.speed,-1)),"N":((-1,2), (-self.speed,-1)), "NE":((1,self.speed), (-self.speed,-1)), "E":((1,self.speed), (-1,2)), "SE":((1,self.speed), (1,self.speed))}

        directionsName = ("S", "SW", "W", "NW", "N", "NE", "E", "SE") 
        
        #move about once every 5 frames
        if random.randrange(0,5) == 2:
            #if no direction is set, set a random one 
            if self.direction == None:
                self.direction = random.choice(directionsName)
            else:
                #get the index of direction in directions list
                a = directionsName.index(self.direction)
                #set the direction to be the same, or one next to the current direction
                b = random.randrange(a - 1,a + 2)
                #if direction index is outside the list, move back to the start
                if b > len(directionsName) - 1: 
                    b = 0
                self.direction = directionsName[b]

            #change relative x to a random number between min x and max x
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1])
            #change relative y to a random number between min y and max y 
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1])

        
            smallOffset = random.random() 
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]

    def borders(self):
        """Ensures that the world is round"""
        #Later, if the agents try to leave the world they will lose points. 

        if self.y < 0:
            self.y = app.height

        if self.y > app.height:
            self.y = 0



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



