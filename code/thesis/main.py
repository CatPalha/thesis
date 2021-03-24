from app import App
from agents import Agent

app = App()


while app.run:

    app.current_menu.display_menu()
    app.main_loop()
    
    
if __name__ == "__main__":
    app.main_loop()


    # #Agents
    # self.midge_num = 5
    # self.pretadors_num = 5
    # #Ecosystem
    # self.trees_num = 3
    # self.water_num = 2
    # #Reproduction
    # self.gen_num = 5
    # self.reproduction_prob = 0.5
    # self.cross_over_prob = 0.3
    # self.mutation_prob = 0.1
    