import pygame
#from pygame_functions import makeTextBox, textBoxInput

class Menu():
    def __init__(self, app):

        self.app = app
        self.mid_width, self.mid_height = self.app.width / 2, self.app.height / 2
        self.menu_running = True
        self.cursor_rect = pygame.Rect(self.mid_width / 2 + 25, self.mid_height - 80, 20, 20)
        self.offset = - 200


    def draw_cursor(self):

        self.app.draw_text('_', 60, self.cursor_rect.x, self.cursor_rect.y)


    def window(self):
 
        self.app.win.blit(self.app.display, (0, 0))
        pygame.display.update()
 
        self.app.reset_keys()
 



class MainMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self, app)

        self.state = "Start"
        self.start_x, self.start_y =  self.mid_width, self.mid_height - 80
        self.parameters_x, self.parameters_y = self.mid_width, self.mid_height - 20
        self.rules_x, self.rules_y = self.mid_width, self.mid_height + 40
        self.cursor_rect_midtop = (self.start_x + self.offset, self.start_y)


    def display_menu(self):

        #just to make sure is True where we need it to be True
        self.menu_running = True
        while self.menu_running:

            self.app.check_events()
            self.check_input()
            self.app.display.fill(self.app.gray)

            self.app.draw_text("Main Menu", 60, self.app.width / 2, 100)
            self.app.draw_text("Start Simulation", 50, self.start_x, self.start_y)
            self.app.draw_text("Parameters", 50, self.parameters_x, self.parameters_y)
            self.app.draw_text("Rules", 50, self.rules_x, self.rules_y)
            self.draw_cursor()
            self.window()


    def move_cursor(self):

        if self.app.DOWN_KEY:

            if self.state == "Start":

                self.cursor_rect.midtop = (self.parameters_x + self.offset, self.parameters_y)
                self.state = "Parameters"

            elif self.state == "Parameters":

                self.cursor_rect.midtop = (self.rules_x + self.offset, self.rules_y)
                self.state = "Rules"

            elif self.state == "Rules":

                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"

        elif self.app.UP_KEY:

            if self.state == "Start":

                self.cursor_rect.midtop = (self.rules_x + self.offset, self.rules_y)
                self.state = "Rules"

            elif self.state == "Parameters":

                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"

            elif self.state == "Rules":

                self.cursor_rect.midtop = (self.parameters_x + self.offset, self.parameters_y)
                self.state = "Parameters"


    def check_input(self):

        #Check if the person want to move the cursor
        self.move_cursor()

        #To check which option the user wants
        if self.app.START_KEY:

            if self.state == "Start":
                self.app.playing = True

            elif self.state == "Parameters":
                self.app.current_menu = self.app.parameters

            elif self.state == "Rules":
                self.app.current_menu = self.app.rules

            
            self.menu_running = False
        


class ParametersMenu(Menu):

    def __init__(self, app):
        Menu.__init__(self, app)

        self.state = "Ecosystem"
        self.ecosystem_x, self.ecosystem_y = self.mid_width, self.mid_height - 80
        self.agents_x, self.agents_y = self.mid_width, self.mid_height - 20
        #self.reproduction_x, self.reproduction_y = self.mid_width, self.mid_height + 40
        self.agent_input_x, self.agent_input_y = self.mid_width, self.mid_height - 100
        # self.wordBox_1 = makeTextBox(self.mid_width, self.mid_height, "Enter number of agents here", 0, 40)
        # self.entry_1 = textBoxInput(self.wordBox_1)


    def display_menu(self):

        self.menu_running = True
        while self.menu_running:

            self.app.check_events()
            self.check_input()
            self.app.display.fill(self.app.gray)
        
            #self.app.draw_text("Parameters", 60, self.app.width / 2, 100)
            # self.app.draw_text("Ecosystem", 50, self.ecosystem_x, self.ecosystem_y)
            # self.app.draw_text("Agents", 50, self.agents_x, self.agents_y)
            #self.app.draw_text("Reproduction", 50, self.reproduction_x, self.reproduction_y)

            #self.draw_cursor()
            self.app.display.fill(self.app.gray)
            self.app.draw_text("Insert the parameters", 60, self.app.width / 2, 100)
            self.app.draw_text("Number of Midges:", 40, self.agent_input_x - 90, self.agent_input_y - 30)
            self.app.draw_text("Number of Pretators:", 40, self.agent_input_x - 70, self.agent_input_y + 30)
            self.app.draw_text("Reproduction probability:" , 40, self.agent_input_x - 18, self.agent_input_y + 90)
            

            self.window()

    def check_input(self):

        if self.app.BACK_KEY:
            self.app.current_menu = self.app.main_menu
            self.menu_running = False

        # elif self.app.UP_KEY or self.app.DOWN_KEY:

        #     if self.state == "Ecosystem":
        #         self.state = "Agents"
        #         self.cursor_rect.midtop = (self.agents_x + self.offset, self.agents_y)
            
        #     elif self.state == "Agents":
        #         self.state = "Ecosystem"
        #         self.cursor_rect.midtop = (self.ecosystem_x + self.offset, self.ecosystem_y)

        # elif self.app.START_KEY:
            
        #     if self.state == "Agents":

        #         self.app.display.fill(self.app.gray)
        #         self.app.draw_text("Choose your parameters", 60, self.app.width / 2, 100)
        #         self.app.draw_text("Number of Agents: ", 50, self.agent_input_x, self.agent_input_y)

        #         self.window()
            
        #     else:
        #         pass

                

    

    
class RulesMenu(Menu):
    def __init__(self, app):
        Menu.__init__(self, app)

        self.rules_x, self.rules_y = self.mid_width, self.mid_height - 80

    def display_menu(self):

        self.menu_running= True
        while self.menu_running:

            self.app.check_events()

            if self.app.BACK_KEY:
                self.app.current_menu = self.app.main_menu
                self.menu_running = False

            self.app.display.fill(self.app.gray)
            self.app.draw_text("Rules", 60, self.app.width / 2, 100)
            self.app.draw_text("TO WRITE THE RULES", 50, self.rules_x, self.rules_y)
            
            self.window()
            







    