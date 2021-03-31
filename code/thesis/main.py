from app import App
from agents import Agent
import parameters

app = App()

midges = []

for i in range(parameters.AGENTS["Number of midges"]): 
    midge = Agent(app)
    midges.append(midge)


mites = []

for i in range(parameters.AGENTS["Number of predators"]): 
    mite = Agent(app)
    mites.append(mite)


while app.run:

    app.current_menu.display_menu()
    app.main_loop(midges, mites)
    
    
if __name__ == "__main__":
    app.main_loop(midges, mites)



    