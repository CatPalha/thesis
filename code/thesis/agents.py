import random

class Agent():

    def __init__(self, app):

        self.app = app
        self.width, self.height = self.app.width, self.app.height
        self.x = random.randrange(100, self.width - 100) 
        self.y = random.randrange(100, self.height - 100) 
        self.speed = random.randrange(2,5) 
        self.move = [None, None] 
        self.direction = None
        self.health = 100

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

        
        #add the relative coordinates to the cells coordinates
        if self.move[0] != None: 
            self.x += self.move[0]
            self.y += self.move[1]

    def borders(self):

        if self.x < 0:
            self.x = self.width

        if self.x > self.width:
            self.x = 0

        if self.y < 0:
            self.y = self.height

        if self.y > self.height:
            self.y = 0



# class Midge(Agent):

#     def __init__(self):
#         Agent.__init__(self, app)
#         self.midge_width, self.midge_height = 350, 150

    


# class Predator(Agent):

#     def __init__(self):
#         Agent.__init__(self, app)
#         self.pretador_width, self.pretador_height = 400, 200



