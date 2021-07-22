import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from systemAI import App

env = App()

def build_model(states, actions):

    model = Sequential()
    model.add(Dense(states, input_dim = states, activation = "relu"))
    model.add(Dense(1, activation = "relu"))
    model.add(Dense(actions, activation = "linear"))

    return model

#6 states, 5 actions
model = build_model(6, 5)
print(model.summary())

from rl.agents import DQNAgent
#Há vários tipos de agentes no keras, é preciso testar isto!!!
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit = 50000, window_length = 1)
    dqn = DQNAgent(model = model, memory = memory, policy = policy,
                    nb_actions = actions, nb_steps_warmup = 10, target_model_update = 1e-2)

    return dqn


dqn = build_agent(model, 5)
dqn.compile(Adam(lr = 1e-3), metrics = ['mae']) #mean abs error
#Como por env aqui???
dqn.fit(env, nb_steps = 50000, visualize = False, verbose = 1)


scores = dqn.test(env, nb_episodes = 100, visualize = False)
print(np.mean(scores.history["episode_reward"]))