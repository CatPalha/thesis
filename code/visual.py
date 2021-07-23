# COLORS FROM https://en.wikipedia.org/wiki/Web_colors#CSS_colors
import math
import pygame
import bioagents

def cv(x, a=0, b=1, c=0, d=255):
    return c + (d - c) * float(x - a) / (b - a)

R2D = 180.0 / math.pi
def deg(rad):
    return rad * R2D

class Visual:
    def __init__(self, env, width=640, height=480, fps=10):
        pygame.init()
        self.size = (self.width, self.height) = (width, height)

        self.ground = pygame.display.set_mode(self.size)
        self.biome = pygame.display.set_mode(self.size)
        self.atmosphere = pygame.display.set_mode(self.size)
        self.atmosphere.set_alpha(10)

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
        color = (50 * (1 + ag.lifecycle.current()), 50 * (1 + ag.lifecycle.current()), 64)
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
        stage = ag.lifecycle.current()
        color = (64, 64, cv(stage,0,3,0,255))
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0), (0, s),  (0.5 * s, s), (s, 0.5 * s), (0.5*s, 0)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_tree(self, ag):
        stage = ag.lifecycle.current()
        color = (64, cv(stage, 0.0, 1, 192, 64), 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.circle(image, color, (0.5 * s, 0.5 * s), 0.5 * s)
        self.biome.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_ground(self):
        YEAR_COLORS = [
            (0, 255, 127),  # SPRING -> SPRING GREEN
            (34, 139,  34), # SUMMER -> FORENST GREEN
            (218, 165,  32),# FALL -> GOLDENROD
            (173, 216, 230) # WINTER -> LIGHT BLUE
        ]
        if hasattr(self.env, 'year'):
            background = YEAR_COLORS[ self.env.year.lifecycle.current()]
        else:
            background = YEAR_COLORS[1]
        self.biome.fill(background)

    def draw_atmosphere(self):
        DAY_COLORS = [
            (255, 165, 0),      # DAWN -> ORANGE
            (255, 248, 220),    # DAY -> CORNSILK
            (75, 0, 130),   # TWILIGHT -> INDIGO
            (25, 25, 112),  # NIGHT -> MIDNIGHT BLUE
        ]
        if hasattr(self.env, 'day'):
            background = DAY_COLORS[ self.env.day.lifecycle.current()]
        else:
            background = DAY_COLORS[1]
        self.atmosphere.fill(background)

    def draw(self):
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
        # self.draw_atmosphere()

        pygame.display.flip()

    def go(self):
        loop = True
        while loop:
            events = [e for e in pygame.event.get()]
            loop = self.update(events)
            self.draw()

            self.clock.tick(self.fps)


