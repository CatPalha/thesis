#Import necessary packages
import random
import pygame
import os
from tkinter import Tk, messagebox

tk = Tk()
tk.wm_withdraw()

#Needed to write on window
#pygame.init()

width, height = 1000, 800
white = (255, 255, 255)
gray = (200,200,200)
black = (0, 0, 0)
fps = 60

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Midge Ecosystem")

def draw_window(name, ):
    """Draw the windows and static agents"""

    for item in folder_name:

    win.fill(white)
    #Place in the window where the midge will be drawn
    agent_name = pygame.image.load(os.pathjoin("folder_name", "item_name")
    # cocoa_tree_1 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    # cocoa_tree_2 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    # cocoa_tree_3 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    # cocoa_tree_4 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    # cocoa_tree_5 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))
    # cocoa_tree_6 = pygame.image.load(os.path.join("Assets", "cocoa_tree.png"))

    # water_1 = pygame.image.load(os.path.join("Assets", "water.png"))
    # water_1 = pygame.transform.scale(water_1, (60, 60))

    # #Static agents
    win.blit(item_name, ((x, y)))
    # win.blit(cocoa_tree_1, ((0,0)))
    # win.blit(cocoa_tree_2, ((300,200)))
    # win.blit(cocoa_tree_3, ((400,200)))
    # win.blit(cocoa_tree_4, ((850,550)))
    # win.blit(cocoa_tree_5, ((750,550)))
    # win.blit(cocoa_tree_6, ((100,0)))



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




def pause_restart():
    """Press to space key to pause and restart the game"""
    loop = True

    while loop:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                loop = False

#             # if event.type == pygame.MOUSEBUTTONDOWN:
#             #     # Set the x, y postions of the mouse click
#             #     x_cursor, y_cursor = event.pos
#             #     print(x_cursor)
#             #     print(y_cursor)

                
#             #     messagebox.showinfo("Midge info", "Generation number: 3 \n Reproduction: False")


def intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    win.fill(gray)

    title_menu = pygame.font.Font('verdana', 20)
    textImg, textRect = text_object("Main Menu", title_menu)
    textRect.center = (width / 2, height - 5)
    win.blit(textImg, textRect)
    pygame.display.update()


        
midges = []

for i in range(1): 
    midge = Agent()
    midges.append(midge)

mites = []

for i in range(1): 
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
            
            #If the user press space bar, the program pauses, if presses again the program restarts
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause_restart()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     # Set the x, y postions of the mouse click
            #     x_cursor, y_cursor = event.pos
            
            #     # print(x_cursor)
            #     # print(y_cursor)

                
    #         #     messagebox.showinfo("Midge info", "Generation number: 3 \n Reproduction: False")

        #intro()
        draw_window()


        for midge in midges: #update all midges agents
            midge.random_movement()
            #midge.borders()
            midge.draw_midge()

        
        for mite in mites: #update all mites agents
            mite.random_movement()
            #mite.borders()
            mite.draw_mite()

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