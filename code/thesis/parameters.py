### CONFIGURATION ###
import random

AGENTS = {
            "Number of midges": 1,
            "Number of predators": 5,
            "Midge Width": 200,
            "Midge Height": 100,
            "Mite Width": 200,
            "Mite Height": 100,
            "Speed": random.randrange(2,5),
            "Initial energy of agents": 100

            
        }


REPRODUCTION = {

                "Probability of reproduction": 0.5,
                "Mutation rate": None,
                "Crossover rate": None

                }


ECOSYSTEM = {
                "Width": 1000,
                "Height": 800,
                "Number of trees": 3,
                "Number of water puddles": 1,
                "x_tree_1": 0,
                "y_tree_1": 0,
                "x_tree_2": 300,
                "y_tree_2": 200,
                "x_water": 100,
                "y_water": 100,
                "Temperature": round(random.uniform(20, 26), 2),
                "Rain": False,
                "Wind": False,
                "x_start": 700,
                "y_start": 700

            }