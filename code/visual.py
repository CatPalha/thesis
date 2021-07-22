import math
import pygame
import bioagents

def cv(x, a=0, b=1, c=0, d=255):
    return c + (d - c) * float(x - a) / (b - a)

R2D = 180.0 / math.pi
def deg(rad):
    return rad * R2D

class Visual:
    def __init__(self, env, width=640, height=480, fps=60):
        pygame.init()
        self.size = (self.width, self.height) = (width, height)
        self.screen = pygame.display.set_mode(self.size)
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
        self.screen.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_mite(self, ag):
        # stage = ag.lifecycle.current()
        color = (128, 64, 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0.25 * s), (0, 0.75 * s),  (s, 0.5 * s)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.screen.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_midge(self, ag):
        stage = ag.lifecycle.current()
        color = (64, 64, cv(stage,0,3,0,255))
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.polygon(image, color, [(0, 0), (0, s),  (0.5 * s, s), (s, 0.5 * s), (0.5*s, 0)])
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.screen.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw_tree(self, ag):
        stage = ag.lifecycle.current()
        color = (64, cv(stage, 0.0, 1, 192, 64), 64)
        s = int(2 * ag.radius)
        image = pygame.Surface( (s, s),  pygame.SRCALPHA)
        image.fill((0,0,0,0))
        pygame.draw.circle(image, color, (0.5 * s, 0.5 * s), 0.5 * s)
        d = deg(ag.heading)
        image = pygame.transform.rotate(image, d)
        self.screen.blit(image, (ag.x - ag.radius, ag.y - ag.radius))

    def draw(self):
        background = (224, 224, 192)
        self.screen.fill(background)
        for ag in self.env.agents.values():
            if isinstance(ag, bioagents.Midge):
                self.draw_midge(ag)
            elif isinstance(ag, bioagents.Mite):
                self.draw_mite(ag)
            elif isinstance(ag, bioagents.Tree):
                self.draw_tree(ag)
            else:
                self.draw_default(ag)

        pygame.display.flip()

    def go(self):
        loop = True
        while loop:
            events = [e for e in pygame.event.get()]
            loop = self.update(events)
            self.draw()

            self.clock.tick(self.fps)


