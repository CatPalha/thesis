from app import App
from agents import Agent

app = App()

midges = []

for i in range(3): 
    midge = Agent()
    midges.append(midge)


mites = []

for i in range(3): 
    mite = Agent()
    mites.append(mite)

for midge in midges:

    midge.random_movement()
    midge.borders()
    app.draw_agent("midge.png", 350, 150, midge.x, midge.y)

for mite in mites:

    mite.random_movement()
    mite.borders()
    app.draw_agent("mite.png", 400, 200, mite.x, mite.y)

while app.run:

    app.current_menu.display_menu()
    app.main_loop()
    
    
if __name__ == "__main__":
    app.main_loop()
