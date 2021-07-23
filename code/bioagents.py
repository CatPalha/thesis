import random
import math

from core import Agent, MobileAgent, BasicLifeCycle

SIZE, SENSOR, PHERHORMONE = GENOTYPE = range(3)
LOW, MEDIUM, HIGH = GENE_RANGE = range(3)

DAY_PARTS = 8 # 1 STEP = 8 HOURS
# EGG, LARVAE, PUPAE, ADULT
MIDGE_LIFECYCLE = BasicLifeCycle(
    3 * DAY_PARTS,  # EGG
    15 * DAY_PARTS, # LARVAE   
    3 * DAY_PARTS,  # PUPAE 
    8 * DAY_PARTS   # ADULT
)

class Midge(MobileAgent):
    def __init__(   self, env, 
                    lifecycle=MIDGE_LIFECYCLE,
                    gene=None, 
                    xy=None, 
                    radius=8, 
                    mass=1, 
                    energy=100.0, 
                    max_vel=None):
        MobileAgent.__init__(self, env, lifecycle=lifecycle, xy=None, radius=8, mass=1, energy=100.0, max_vel=None)

        self.sensor_range = 4 * self.radius
        if gene is None:
            self.gene = list()
            for gene in GENOTYPE:
                self.gene.append(random.choice(GENE_RANGE))
        else:
            self.gene = gene

    def behave(self):
        MobileAgent.behave(self)

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
class Mite(MobileAgent):
    def __init__(self, env, lifecycle=MITE_LIFECYCLE):
        MobileAgent.__init__(self, env, lifecycle=lifecycle, radius=8)
        self.sensor_range = 2 * self.radius

    def behave(self):
        MobileAgent.behave(self)
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
TREE_LIFECYCLE = BasicLifeCycle(
    120 * DAY_PARTS,
    240 * DAY_PARTS
)

class Tree(Agent):
    def __init__(self, env, lifecycle=TREE_LIFECYCLE, xy=None, radius=16):
        self.radius = radius
        if xy is None:
            self.x, self.y = env.get_random_position(radius)
        else:
            self.x, self.y = xy

        Agent.__init__(self, env, lifecycle=lifecycle)
        
# DAWN, DAY, TWILIGHT, NIGHT
DAY_CYCLE = BasicLifeCycle(
    2,  # DAWN
    2,  # DAY
    2,  # TWILIGHT
    2   # NIGHT
)
class Day(Agent):
    def __init__(self, env, lifecycle=DAY_CYCLE):
        Agent.__init__(self, env, lifecycle=lifecycle)

# SPRING, SUMMER, FALL, WINTER
YEAR_CYCLE = BasicLifeCycle(
    90 * DAY_PARTS,  # SPRING
    90 * DAY_PARTS,  # SUMMER
    90 * DAY_PARTS,  # FALL
    90 * DAY_PARTS,  # WINTER
)
class Year(Agent):
    def __init__(self, env, lifecycle=YEAR_CYCLE):
        Agent.__init__(self, env, lifecycle=lifecycle)