import random
import math

from core import Agent, BasicLifeCycle

SIZE, SENSOR, PHERHORMONE = GENOTYPE = range(3)
LOW, MEDIUM, HIGH = GENE_RANGE = range(3)

DAY_PARTS = 3 # 1 STEP = 8 HOURS
# EGG, LARVAE, PUPAE, ADULT
MIDGE_LIFECYCLE = BasicLifeCycle(
    3 * DAY_PARTS,  # EGG
    15 * DAY_PARTS, # LARVAE   
    3 * DAY_PARTS,  # PUPAE 
    8 * DAY_PARTS   # ADULT
)

class Midge(Agent):
    def __init__(self, env, gene=None, xy=None, radius=8, mass=1, energy=100.0, max_vel=None):
        Agent.__init__(self, env, xy=None, radius=8, mass=1, energy=100.0, max_vel=None)
        self.lifecycle = MIDGE_LIFECYCLE
        self.sensor_range = 4 * self.radius
        if gene is None:
            self.gene = list()
            for gene in GENOTYPE:
                self.gene.append(random.choice(GENE_RANGE))
        else:
            self.gene = gene

    def behave(self):
        Agent.behave(self)

        self.acc = 1.0

        detected = self.env.scan_at(self.x, self.y, self.sensor_range) - {self.id}        
        detected_mites = self.env.filter(detected, lambda ag: isinstance(ag, Mite))
        detected_trees = self.env.filter(detected, lambda ag: isinstance(ag, Tree))
        if len(detected_mites) > 0:
            pos = self.env.map(detected_mites, lambda ag: (ag.x, ag.y))
            n = len(pos)
            x = sum(p[0] for p in pos) / n
            y = sum(p[1] for p in pos) / n
            self.head_to(x, y)
            self.heading *= -1.0
            self.acc = 2.0
        elif len(detected_trees) > 0:
            pos = self.env.map(detected_trees, lambda ag: (ag.x, ag.y))
            n = len(pos)
            x = sum(p[0] for p in pos) / n
            y = sum(p[1] for p in pos) / n
            self.head_to(x, y)
        else:
            d = random.gauss(0, math.pi )
            self.heading += 0.125 * d



MITE_LIFECYCLE = BasicLifeCycle(
    360 * DAY_PARTS
)
class Mite(Agent):
    def __init__(self, env):
        Agent.__init__(self, env, radius=8)
        self.lifecycle = MITE_LIFECYCLE
        self.sensor_range = 2 * self.radius

    def behave(self):
        Agent.behave(self)
        detected = self.env.scan_at(self.x, self.y, self.sensor_range) - {self.id}
        detected = self.env.filter(detected, lambda ag: isinstance(ag, Midge))
        if len(detected) > 0:
            pos = self.env.map(detected, lambda ag: (ag.x, ag.y))
            n = len(pos)
            x = sum(p[0] for p in pos) / n
            y = sum(p[1] for p in pos) / n
            self.head_to(x, y)
        else:
            d = random.gauss(0, math.pi )
            self.heading += 0.125 * d

        self.acc = 1.0


# BLOOMING, NOT_BLOOMING
TREE_LIVECYCLE = BasicLifeCycle(
    120 * DAY_PARTS,
    240 * DAY_PARTS
)

class Tree(Agent):
    def __init__(self, env, xy=None):
        Agent.__init__(self, env, xy=xy, radius=16, mass=1000, energy=100.0, max_vel=0)
        self.lifecycle = TREE_LIVECYCLE