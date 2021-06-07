#Import necessary packages
import random
import pygame
import os
import parameters



class App:
    def __init__(self):

        self.run = True

        self.width, self.height = parameters.ECOSYSTEM["Width"], parameters.ECOSYSTEM["Height"]
        self. white = (255, 255, 255)
        self.fps = 60

        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Midge Ecosystem")
        self.clock = pygame.time.Clock() 

        self.x = random.randrange(200, parameters.ECOSYSTEM["Width"] - 200) 
        self.y = random.randrange(200, parameters.ECOSYSTEM["Height"] - 200) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None 
        self.score = 470
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




    def draw_midge(self):
        #Agent transformations: size and rotation
        midge = pygame.image.load(os.path.join("Assets", "midge.png"))
        
        midge = pygame.transform.scale(midge, (parameters.AGENTS["Midge Width"], parameters.AGENTS["Midge Height"]))

        self.win.blit(midge, (self.x, self.y))
        

    def draw_mite(self):
        #Agent transformations: size and rotation
        mite = pygame.image.load(os.path.join("Assets", "mite.png"))

        mite = pygame.transform.scale(mite, (parameters.AGENTS["Mite Width"], parameters.AGENTS["Mite Height"]))

        self.win.blit(mite, (self.x, self.y))



    def movement(self):

        directions = {"SW":((-self.speed,-1), (1,self.speed)), "NW":((-self.speed,-1), (-self.speed,-1)), "NE":((1,self.speed), (-self.speed,-1)), "SE":((1,self.speed), (1,self.speed))}
        #possible directions
        directionsName = ("SW", "NW", "NE", "SE") 
        
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

        # #Setting the borders, round world
        if self.x < 0 or self.x > self.width or self.y < 0 or self.y > self.height: 

            if self.y < 0:
                self.y = self.height

            if self.y > self.height:
                self.y = 0

            smallOffset = random.random() 
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]



    def random_movement(self):

        #((min x, max x)(min y, max y))
        directions = {"S":((-1,2), (1,self.speed)), "SW":((-self.speed,-1), (1,self.speed)), "W":((-self.speed,-1), (-1,2)), "NW":((-self.speed,-1), (-self.speed,-1)),"N":((-1,2), (-self.speed,-1)), "NE":((1,self.speed), (-self.speed,-1)), "E":((1,self.speed), (-1,2)), "SE":((1,self.speed), (1,self.speed))}
        #possible directions
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

        # #Setting the borders, round world
        if self.x < 0 or self.x > self.width or self.y < 0 or self.y > self.height: 

            if self.y < 0:
                self.y = self.height

            if self.y > self.height:
                self.y = 0

            smallOffset = random.random() 
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]


    def main(self, midges, mites):

        while self.run:

            self.clock.tick(self.fps)

            for event in pygame.event.get():
            ##If the user pressi X, quit the program
                if event.type == pygame.QUIT: 
                    self.run = False

            self.draw_window()

            ## PRETADATORS
            for mite in mites: 
                mite.random_movement()
                mite.draw_mite()

            ## MIDGES
            for midge in midges: 
                midge.movement()
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


            pygame.display.update() #update display

        pygame.quit()

##############################################################
##############################################################


if __name__ == "__main__":

    app = App()

    midges = []

    for i in range(parameters.AGENTS["Number of midges"]): 
        midge = App()
        midges.append(midge)

    mites = []

    for i in range(parameters.AGENTS["Number of predators"]): 
        mite = App()
        mites.append(mite)

   
    app.main(midges, mites)



