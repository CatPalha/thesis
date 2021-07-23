core.py:

- LifeCycle

    Initialize age = 0

    current: returns the updated age

    step: in each step increases the age by 1

- BasicLifeCycle: Inherit LifeCycle

    Initialize repeating = True, 
            durations, 
            change_stage = list(): goes to durations and appends when to change the stage

            cycle_duration: last position of change_stage
            current_stage = 0
    
    current: returns the current stage

    step: calls LifeCycle step function (increases age by 1)
          calculates cycle_age as being the remainder of the division of age by cycle_duration

          if cycle_age lower than the last change_state AND cycle_age greater than current stage in change_stage
            current_stage is increased by 1
          elif repeats the process and keeps the current_stage = 0
          else does nothing

- Agent: arg: env, lifecycle = None, energy = 1.0

    Initialize age = 0, energy, lifecycle, env and id: by using add_agent, adds an agent to the env

    physics: does nothing

    metabolims: increases the age by 1 and steps on lifecycle

    set_lifecycle: arg: lf
        set lifecycle as lf

    do: receives an action and parameters as arguments and does that action based on parameters

    sense: receives a sensor and parameters and does nothing

    behave: does nothing

    step: if energy greater than zero and an env exists and a lifecycle exists
            calls metabolims, behave, physics
    
    __repr__ when printed an agents shows the id, the age and the stage


- MobileAgent: Inherit Agent

    Initialize: args: env, lifecycle = None, xy = None, radius = 8, mass, energy = 100.0, max_vel = None

        if xy is None: goes to env and get_random_position(radius)
        else x,y is the xy

        x, y, heading = 0, vel = 0, acc = 0, radius =radius, mass = mass

        if max_vel is None set max_vel = radius
        else max_vel is max_vel

        energy = energy

        initilize the class Agent with an env and a lifecycle


    physics: increases acc to vel
             clip(vel, 0, max_vel): keeps the vel between 0 and max_vel
             acc = 0
             d: vector that given the heading and the vel, tells the new position of the agent
             dest: puts the agent in the new position
             within_bounds: insures thta the agent does not leave the env bounderies.
             if the agents respects the bounderies of the env and has no other agents in his surounding
                it moves to the new position

    behave: does nothing

    head_to: args: x, y)
            gives the direction of the movement, the heading

    
    __repr__ when printed a MobileAgent it shows the id, the age, the energy and the stage


    - RandomWalker: Inherit MobileAgent

        behave: makes the agent move randomly in the heading direction with an acc

    - Environment

        initialize: args: width = 1024 and height = 1024
            age = 0, width = width, height = height and agents = dict()

        
        map: args: ag_ids, func
            given agents ids apply a function to every id and returns a list with the result of the function for every id

        filter: returns a list of agents ids that verify a certain condition 

        add_agent: receives agent as arg and gives it an id and puts it in the env

        step: increses the age of the env by 1 (internal clock on env)

        scan_at: returns a set of agents ids that have a position that are within the agent radius
                 the agent needs to have a position, for instances, year is an agent and does not have a position

        get_random_position: gets a random position x and y
                             insures that there is no other agents in that random position
                             insures thta this random position is within the env

        __repr__: when printed the env returns the age of env, and the agent inside it.

#######################

bioagents.py

declares a SIZE, SENSOR, PHERHORME  with range 3 -> GENOTYPE ARRAY
LOW, MEDIUM, HIGH with range 3 -> GENE_RANGE ARRAY

DAY_PARTS = 8: each step has 8 hours

MIDGE_LIFECYCLE: uses BasicLifeCycle to define the stages: egg, larvae, pupar and adult
                egg lasts 3 days
                larvae lasts 15 days
                pupae lasts 3 days
                adult lasts 8 days

- Midge: Inherit MobileAgent

    Initialize with args: env, lifecycle = MIDGE_LIFECYCLE, gene, xy, radius, mass, energy, max_vel
                          Initializes the MobileAgent

                          sensor_range is 4 times the radius

                          if the gene is None creates a gene list and append random values from the GENE_RANGE to the GENOTYPE
                          else uses the existant gene


    behave: calls the bahave frunction from MobileAgent

            sets acc = 1.0

            detects if there are other agents inside its radius
            detects if those agents are mites or trees

            if detects mites inside its radius flees with a greater acc
            elif detets trees go to the trees
            else keep walking randomly


MITE_LIFECYCLE: BasicLifeCycle com 360 dias, and each day has the DAY_PARTS

- Mite: Inherit MobileAgent

        Initializes MobileAgent
