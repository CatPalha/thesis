import torch
import random
import numpy as np
from collections import deque
from RL import App

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0
        #controlls the randomness
        self.epsilon = 0
        #discount rate
        self.gamma = 0
        self.memory = deque(maxlen = MAX_MEMORY)



    def get_state(self, app):
        pass

    
    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass


def train():
    #To plot later
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    app = App()

    while True:
        #get old state
        state_old = agent.get_state(app)
        #get move, this is the action
        final_move = agent.get_action(state_old)
        #perform move and get new state
        reward, done, score = app.main(final_move)
        state_new = agent.get_state(app)
        #train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        #remmember all of this
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            #train the long memory and plot the results
            app.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                #agent.model.save()
            print("Game: ", agent.n_games, "Score: ", score, "Record: ", record)

            #TODO: plots

            




#############


if __name__ == '__main__':
    train()