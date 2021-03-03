#Import necessary packages
import random
import pygame
import os

pygame.init()

width, height = 1000, 800
white = (255, 255, 255)
gray = (200,200,200)
black = (0, 0, 0)
fps = 60

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Midge Ecosystem")

def draw_window():
    """Draw the windows and static agents"""
    win.fill(white)
    #Place in the window where the midge will be drawn
    cocoa_tree_1 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    cocoa_tree_2 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    cocoa_tree_3 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    cocoa_tree_4 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    cocoa_tree_5 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    cocoa_tree_6 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))

    water_1 = pygame.image.load(os.path.join("Assets", "water.png"))
    water_1 = pygame.transform.scale(water_1, (60, 60))

    #Static agents
    win.blit(cocoa_tree_1, ((0,0)))
    win.blit(cocoa_tree_2, ((300,200)))
    win.blit(cocoa_tree_3, ((400,200)))
    win.blit(cocoa_tree_4, ((850,550)))
    win.blit(cocoa_tree_5, ((750,550)))
    win.blit(cocoa_tree_6, ((100,0)))
    win.blit(water_1, ((385, 285)))



class Agent:
    def __init__(self):
        self.x = random.randrange(10, width - 10) #x position
        self.y = random.randrange(10, height - 10) #y position
        self.speed = random.randrange(2,5) #cell speed
        self.move = [None, None] #realtive x and y coordinates to move to
        self.direction = None #movement direction

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
        

    def wander(self):

        #((min x, max x)(min y, max y))
        directions = {"S":((-1,2), (1,self.speed)), "SW":((-self.speed,-1), (1,self.speed)), "W":((-self.speed,-1), (-1,2)), "NW":((-self.speed,-1), (-self.speed,-1)),"N":((-1,2), (-self.speed,-1)), "NE":((1,self.speed), (-self.speed,-1)), "E":((1,self.speed), (-1,2)), "SE":((1,self.speed), (1,self.speed))}
        directionsName = ("S", "SW", "W", "NW", "N", "NE", "E", "SE") #possible directions
        
        if random.randrange(0,5) == 2: #move about once every 5 frames
            if self.direction == None: #if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction) #get the index of direction in directions list
                b = random.randrange(a - 1,a + 2) #set the direction to be the same, or one next to the current direction
                if b > len(directionsName) - 1: #if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]

            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) #change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) #change relative y to a random number between min y and max y
        
        if self.x < 5 or self.x > width - 5 or self.y < 5 or self.y > height - 5: #if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > width - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > height - 5:
                self.direction = "N"
            smallOffset = random.random() #Random floating-point number between 0 and 1 ("Tiny number")
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1]) + smallOffset
        
        if self.move[0] != None: #add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]


def pause_restart_game():
    """Press to space key to pause and restart the game"""
    loop = True

    while loop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                loop = False




midges = []

for i in range(5): #generate n cells
    midge = Agent()
    midges.append(midge)

mites = []

for i in range(5): #generate n cells
    mite = Agent()
    mites.append(mite)

def main():
    #limit FPS
    clock = pygame.time.Clock() 

    run = True
    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            #If the user pressi X, quit the program
            if event.type == pygame.QUIT: 
                run = False
            
            if event.type == pygame.KEYDOWN:
                pause_restart_game()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if restart_button.isOver(pos):
            #         print("Restarted the simulation")

        draw_window()

        for midge in midges: #update all midges agents
            midge.wander()
            midge.draw_midge()
        
        for mite in mites: #update all mites agents
            mite.wander()
            mite.draw_mite()

        # restart_button.draw_button(win)
        # pause_button.draw_button(win)

        pygame.display.update() #update display

    pygame.quit()
    

#This guarantees the function main only runs when this files runs, if I want to run from somewhere else I need to delete this
if __name__ == "__main__":
    main()



"""
class Button():
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, win, outline = None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2,self.y - 2,self.width + 4,self.height + 4), 0)
            
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('verdana', 20)
            text = font.render(self.text, 1, black)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
          
        return False

#Start Button
restart_button = Button(gray, 930, 0, 70, 40, 'Restart')
pause_button = Button(gray, 850, 0, 70, 40, 'Pause')

class Agent:
    #Posso ter varios agentes, é só defenir instanciar uma classe para cada agente.
    def ___init___(self, width, height, health = 100):
        self.width = width
        self.height = height
        self.health = health
        self.agent_img = None

        # self.positions = [((width / 2), (height / 2))]
        # self.direction = random.choice([up, down, left, rigth])

    def draw_agent(self, window):
        #It can be a midge, a mite or a cocoa tree.
        window.blit(self.ship_img, (self.width, self.height))

    def get_width(self):
        return self.agent_img.get_width()
    
    def height(self):
        return self.agent_img.height()

class Midge(Agent):

    def __init__(self, width, height, health = 100):
        super().__init__(width, height, health)
        self.ship_img = midge
        self.max_health = health

    def midge_movement(self, velocity):
        self.height += velocity

class Predator(Agent):

    def __init__(self, width, height, health = 100):
        super().__init__(width, height, health)
        self.ship_img = mite
        self.max_health = health



def moviment():
    pass

def reset(self):
    pass

def reset(self):
    self,positions = [((width / 2), (height / 2))]
    self.direction = random.choice([up, down, left, rigth])

class Food(object):

    def ___init___(self):
        pass

    def cacoa_tree(self, surface):
        pass

"""