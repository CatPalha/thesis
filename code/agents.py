import random
import parameters
import pygame
import os
from system import App

app = App()

class Midge:

    def __init__(self, app):  

        self.app = app
        self.x = random.randrange(200, parameters.ECOSYSTEM["Width"] - 200) 
        self.y = random.randrange(200, parameters.ECOSYSTEM["Height"] - 200) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None
        self.energy = 470 
        #self.vel = 1

    def draw_midge(self):
      
        midge = pygame.image.load(os.path.join("Assets", "midge.png"))
        
        midge = pygame.transform.scale(midge, (parameters.AGENTS["Midge Width"], parameters.AGENTS["Midge Height"]))

        app.win.blit(midge, (self.x, self.y))
    
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

        if self.y < -35:
            self.y = 751

        if self.y > 751:
            self.y = -35

        if self.x < -91:
            self.x = 889
        
        if self.x > 889:
            self.x = -91
    

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

        if self.y < -35:
            self.y = 751

        if self.y > 751:
            self.y = -35

        if self.x < -91:
            self.x = 889
        
        if self.x > 889:
            self.x = -91