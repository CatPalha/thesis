### CONFIGURATION ###
import random

AGENTS = {
            "Number of midges": 1,
            "Number of predators": 3,
            "Midge Width": 200,
            "Midge Height": 100,
            "Mite Width": 200,
            "Mite Height": 100,
            "Speed": random.randrange(2,5),

            
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
                "x_tree_1": 100,
                "y_tree_1": 100,
                "x_tree_2": 400,
                "y_tree_2": 400,
                "x_water": 200,
                "y_water": 200,
                "Temperature": round(random.uniform(20, 26), 2),
                "Rain": False,
                "Wind": False,
                "Initial score": 470

            }