#! /usr/bin/env python3
import random

import core
import bioagents
import visual

def test_01():
    env = core.Environment()
    for i in range(5):
        ag = core.RandomWalker(env,
            min_x=8, max_x=env.width-8,
            min_y=8, max_y=env.height-8)    
        cycle = core.BasicLifeCycle(100, 300, 500, 300)
        ag.set_lifecycle(cycle)

    for t in range(20):
        env.step()
        print(env)

def test_02():
    env = core.Environment()
    for i in range(50):
        ag = core.RandomWalker(env,
            min_x=8, max_x=env.width-8,
            min_y=8, max_y=env.height-8)    
        cycle = core.BasicLifeCycle(100, 300, 500, 300)
        ag.set_lifecycle(cycle)

    vis = visual.Visual(env, env.width, env.height)
    vis.go()

def test_03():
    env = core.Environment()
    cycle = core.BasicLifeCycle(100, 300, 500, 300)

    env.year = bioagents.Year(env)
    env.day = bioagents.Day(env)

    # for i in range(5):
    #     ag = core.RandomWalker(env)    
    #     ag.set_lifecycle(cycle)
    
    for i in range(20):
        case = random.randint(0,2)
        if case == 0:
            ag = bioagents.Tree(env)
            #pass   
        elif case == 1:
            ag = bioagents.Mite(env)
            #pass
        else:
            ag = bioagents.Midge(env)

    vis = visual.Visual(env, env.width, env.height, fps=60)
    vis.go()

def test_04():
    env = core.Environment()
    env.day = bioagents.Day(env)
    env.year = bioagents.Year(env)
    vis = visual.Visual(env, env.width, env.height, fps=60)
    vis.go()


if __name__ == "__main__":
    random.seed()
    test_03()
