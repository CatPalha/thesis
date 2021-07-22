import math
import random

class LifeCycle:
    def __init__(self):
        self.age = 0

    def current(self):
        return None

    def step(self):
        self.age += 1

class BasicLifeCycle(LifeCycle):
    def __init__(self, *durations):
        LifeCycle.__init__(self)
        self.repeating = True
        self.durations = durations
        self.change_stage = list()
        sum = 0
        for i,d in enumerate(self.durations):
            sum += d
            self.change_stage.append(sum)

        self.cycle_duration = self.change_stage[-1]
        self.current_stage = 0

    def current(self):
        return self.current_stage

    def step(self):
        LifeCycle.step(self)
        cycle_age = self.age % self.cycle_duration
        if cycle_age < self.change_stage[-1] and cycle_age >= self.change_stage[ self.current_stage ]:
            self.current_stage += 1
        elif self.repeating:
            self.current_stage = 0
        else:
            pass

EAST = (1,0)
WEST = (-1, 0)
NORTH = (0, -1)
SOUTH = (0, 1)
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Agent:
    def __init__(self, env, xy=None, radius=8, mass=1, energy=100.0, max_vel=None):

        if xy is None:
            retries = 100
            x = random.randrange(radius, env.width - radius)
            y = random.randrange(radius, env.height - radius)
            while retries > 0 and len(env.scan_at(x,y, radius)) > 0:
                x = random.randrange(radius, env.width - radius)
                y = random.randrange(radius, env.height - radius)
                retries -= 1
        else:
            x,y = xy
        self.x = x
        self.y = y

        self.heading = 0

        self.vel = 0
        self.acc = 0

        self.radius = radius

        self.mass = mass

        if max_vel is None:
            self.max_vel = self.radius
        else:
            self.max_vel = max_vel
        
        self.age = 0

        self.energy = energy

        self.lifecycle = None

        self.env = env
        self.id = env.add_agent(self)
        
    def physics(self):
        self.vel += self.acc
        self.vel = clip(self.vel, 0, self.max_vel)
        self.acc = 0
        d = (math.cos(self.heading) * self.vel, -math.sin(self.heading) * self.vel)

        dest = (self.x + d[0], self.y + d[1])

        within_bounds = self.radius <= dest[0] <= self.env.width - self.radius and \
            self.radius <= dest[1] <= self.env.height - self.radius
        if within_bounds and len(self.env.scan_at(dest[0], dest[1], self.radius) - {self.id}) == 0:
            self.x += d[0]
            self.y += d[1]

    def metabolism(self):
        self.age += 1
        self.lifecycle.step()

    def set_lifecycle(self, lf):
        self.lifecycle = lf

    def do(self, action, parameters):
        action(*parameters)

    def sense(self, sensor, parameters):
        pass

    def behave(self):
        pass

    def head_to(self, x, y):
        self.heading = math.atan2(y, x)

    def step(self):
        if self.energy > 0 and self.env is not None and self.lifecycle is not None:
            self.metabolism()
            self.behave()
            self.physics()

    def __repr__(self):
        return f"[{self.id} age: {self.age} energy: {self.energy} stage: {self.lifecycle.current()} ]"


class RandomWalker(Agent):
    # def __init__(self, env):
    #     Agent.__init__(self, env)

    def behave(self):
        Agent.behave(self)
        d = random.gauss(0, math.pi )
        self.heading += 0.125 * d
        self.acc = (self.lifecycle.current() + 1)

class Environment:
    def __init__(self, width=1024, height=1024):
        self.age = 0
        self.width = width
        self.height = height
        self.agents = dict()

    def map(self, ag_ids, func):
        ags = [self.agents[i] for i in ag_ids if i in self.agents.keys()]
        return  [func(ag) for ag in ags]

    def filter(self, ag_ids, pred):
        ags = [self.agents[i] for i in ag_ids if i in self.agents.keys()]
        return [ag.id for ag in ags if pred(ag)]

    def add_agent(self, agent):
        agent_id = len(self.agents)
        self.agents[agent_id] = agent
        return agent_id

    def step(self):
        self.age += 1
        for ag in self.agents.values():
            ag.step()

    def scan_at(self, x, y, r):
        return set(ag.id for ag in self.agents.values() if math.hypot(ag.x - x, ag.y - y) < ag.radius + r)

    def __repr__(self):
        split = "\n\t"
        return f"[{self.age}]{split.join(str(ag) for ag in self.agents.values())}"

def clip(x, a, b):
    if x < a:
        return a
    elif b < x:
        return b
    return x