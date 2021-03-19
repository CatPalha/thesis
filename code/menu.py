import pygame

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

                self.app.win.fill(self.app.white)
                pygame.display.set_caption("Midge Ecosystem")

                self.app.draw_agent("cocoa_tree.png", 133, 135, 300, 200)
                self.app.draw_agent("cocoa_tree.png", 133, 135, 500, 200)
                self.app.draw_agent("water.png", 100, 80, 425, 300)

                # for midge in midges:

                #     midge.random_movement()
                #     midge.borders()
                #     self.draw_agent("midge.png", 350, 150, midge.x, midge.y)

                # for mite in mites:

                #     mite.random_movement()
                #     mite.borders()
                #     self.draw_agent("mite.png", 400, 200, mite.x, mite.y)

                
                pygame.display.update()
                self.app.reset_keys()

            elif self.state == "Parameters":
                pass

            elif self.state == "Rules":
                pass

            
            self.menu_running = False
        
