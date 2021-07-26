# COLORS FROM https://en.wikipedia.org/wiki/Web_colors#CSS_colors
import math
import pygame
import bioagents

def cv(x, a=0, b=1, c=0, d=255):
    return c + (d - c) * float(x - a) / (b - a)

R2D = 180.0 / math.pi

def deg(rad):
    return rad * R2D

COLOR = {
    'white':        (255, 255, 255),
    'black':        (  0,   0,   0),
    'spring_green': (  0, 255, 127),    # SPRING -> SPRING GREEN
    'forest_green': ( 34, 139,  34),    # SUMMER -> FORENST GREEN
    'goldenrod':    (218, 165,  32),    # FALL -> GOLDENROD
    'light_blue':   (173, 216, 230),    # WINTER -> LIGHT BLUE

    'orange':       (255, 165,   0),      # DAWN -> ORANGE
    'cornsilk':     (255, 248, 220),    # DAY -> CORNSILK
    'indigo':       ( 75,   0, 130),   # TWILIGHT -> INDIGO
    'twilight':     (199, 157, 215),
    'midnight_blue':( 25,  25, 112),  # NIGHT -> MIDNIGHT_BLUE
}

class Visual:
    def __init__(self, env, width=640, height=480, fps=10):
        pygame.init()
        self.size = (self.width, self.height) = (width, height)

        self.surface = pygame.display.set_mode(self.size)
        self.ground = pygame.Surface(self.size, pygame.SRCALPHA)
        self.biome = pygame.Surface(self.size, pygame.SRCALPHA)
        self.atmosphere = pygame.Surface(self.size, pygame.SRCALPHA)
        self.atmosphere.set_alpha(64)

        self.fps = fps
        self.clock = pygame.time.Clock()
        self.env = env
        self.paused = True

    def update(self, events):
        if any(e.type == pygame.QUIT for e in events):
            return False
        if any(e.type == pygame.KEYUP and e.key == pygame.K_SPACE for e in events):
            self.paused = not self.paused
        if not self.paused:
            self.env.step()
        return True

    def draw_default(self, ag):
        color = (50 * (1 + ag.lifecycle.current_stage), 50 * (1 + ag.lifecycle.current_stage), 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0.5 * s), (0.5*s, s), (s, 0.5 * s),  (0.5*s, 0)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_mite(self, ag):
        # stage = ag.lifecycle.current()
        color = (128, 64, 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0.25 * s), (0, 0.75 * s),  (s, 0.5 * s)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_midge(self, ag):
        stage = ag.lifecycle.current_stage
        
        color = (64, 64, cv(stage,0,3,0,255))
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0), (0, s),  (0.5 * s, s), (s, 0.5 * s), (0.5*s, 0)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_tree(self, ag):
        stage = ag.lifecycle.current_stage
        color = (64, cv(stage, 0.0, 1, 192, 64), 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.circle(image, color, (0.5 * s, 0.5 * s), 0.5 * s)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_cycle(self, surface, cycle, colors, y=0, height=16):
        last_pos = 0
        for i,t in enumerate(cycle.change_stage):
            pos = int(self.width * t / cycle.total_duration())
            color = COLOR[colors[i]]
            rect = (last_pos, y, pos, height)
            pygame.draw.rect(surface, color, rect)
            last_pos = pos
        p = int(self.width * cycle.cycle_age() / cycle.total_duration())
        pygame.draw.rect(surface, COLOR['black'], (0, y, p, height))
        # pygame.draw.rect(surface, (0,0,0), (0, y, p, height), height // 3)

    def draw_ground(self):
        YEAR_COLORS = [
            'spring_green',
            'forest_green',
            'goldenrod',
            'light_blue' ]
        # cycle = self.env.year.lifecycle
        # color = COLOR[YEAR_COLORS[ cycle.current_stage ]]
        # p = int(self.width * cycle.cycle_age() / cycle.total_duration())
        # pygame.draw.rect(self.biome, color, (0, 0, p, 16))
        self.draw_cycle(self.atmosphere, self.env.year.lifecycle, YEAR_COLORS, y=0)

    def draw_atmosphere(self):
        DAY_COLORS = [
            'orange',
            'cornsilk',
            'twilight',
            'midnight_blue'
        ]
        # cycle = self.env.day.lifecycle
        # color = COLOR[DAY_COLORS[ cycle.current_stage ]]
        # p = int(self.width * cycle.cycle_age() / cycle.total_duration())
        # pygame.draw.rect(self.biome, color, (0, 16, p, 16))
        self.draw_cycle(self.atmosphere, self.env.day.lifecycle, DAY_COLORS, y=16)

    def draw(self):
        self.ground.fill(COLOR['white'])
        self.biome.fill(COLOR['white'])
        self.atmosphere.fill(COLOR['white'])
        self.draw_ground()
        for ag in self.env.agents.values():
            if isinstance(ag, bioagents.Midge):
                self.draw_midge(ag)
            elif isinstance(ag, bioagents.Mite):
                self.draw_mite(ag)
            elif isinstance(ag, bioagents.Tree):
                self.draw_tree(ag)
            elif isinstance(ag, bioagents.Year) or isinstance(ag, bioagents.Day):
                pass
            else:
                self.draw_default(ag)
        self.draw_atmosphere()

        self.surface.blit(self.ground, (0,0))
        self.surface.blit(self.biome, (0,0))
        self.surface.blit(self.atmosphere, (0,0))
        pygame.display.flip()
        pygame.display.set_caption('Ecosystem')

    def go(self):
        loop = True
        while loop:
            events = [e for e in pygame.event.get()]
            loop = self.update(events)
            self.draw()

            self.clock.tick(self.fps)


