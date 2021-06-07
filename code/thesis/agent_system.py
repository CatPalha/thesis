import random
#import pygame

class Agent:
    def __init__(self):
        self.x = random.randrange(20, width - 20) 
        self.y = random.randrange(20, height - 20) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None 

    def draw_midge(self):
        #Agent transformations: size and rotation
        midge = pygame.image.load(os.path.join("Assets", "midge.png"))
        
        midge_width, midge_height = 350, 150
        midge = pygame.transform.scale(midge, (midge_width, midge_height))

        win.blit(midge, (self.x, self.y))
        

    def draw_mite(self):
        #Agent transformations: size and rotation
        mite = pygame.image.load(os.path.join("Assets", "mite.png"))

        mite_width, mite_height = 400, 200
        mite = pygame.transform.scale(mite, (mite_width, mite_height))

        win.blit(mite, (self.x, self.y))

    def draw_tree(self):

        cocoa_tree = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))

        win.blit(cocoa_tree, ((self.x, self.y)))
        

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
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height: 
            if self.x < 0:
                self.x = 0

            if self.x > width:
                self.x = width

            if self.y < 0:
                self.y = height

            if self.y > height:
                self.y = 0

            smallOffset = random.random() 
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]

    # def borders(self):
    #     """Ensures that the world is round"""
    #     #if self.x < 0 or self.x > width or self.y < 0 or self.y > height:

    #     if self.x < 0:
    #         self.x = 0

    #     if self.x > width:
    #         self.x = width

    #     if self.y < 0:
    #         self.y = height

    #     if self.y > height:
    #         self.y = 0