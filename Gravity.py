import pygame
import random
import math
import sys

from pygame.locals import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Particle:
    def __init__(self, x, y, speedx, speedy, mass):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.mass = mass
        self.radius = math.sqrt(self.mass)


class Gravity():
    def __init__(self, screen_width, screen_height):
        # Set the size of the surface
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.particles = []
        self.create_particles()
        pygame.init()
        self.Surface = pygame.display.set_mode((self.SCREEN_WIDTH,
                                                self.SCREEN_HEIGHT))
        self.gameloop()

    def create_particles(self):
        while True:
            ParticleNumber = raw_input("Enter how many particles to draw: ")
            # Make sure the number supplied is an int otherwise ask again.
            try:
                ParticleNumber = int(ParticleNumber)
                break
            except:
                print "\nWell, now.  Let's try that again."

        # Create a large particle in the center of the system
        self.particles.append(Particle(600, 300, 0.0, 0.0, 1000))

        # Create some random little particles.
        for x in range(ParticleNumber):
            self.particles.append(Particle(random.randint(10, 1190),
                                           random.randint(10, 690),
                                           random.uniform(-1.5, 1.5),
                                           random.uniform(-1.5, 1.5),
                                           random.uniform(1, 10)))

    def gameloop(self):
        while True:
            self.get_input()
            self.move()
            self.collision_detect()
            self.draw()

    def get_input(self):
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keystate[K_ESCAPE]:
                pygame.quit()
                sys.exit()

    def move(self):
        for P in self.particles:
            for P2 in self.particles:
                if P != P2:
                    XDiff = P.x - P2.x
                    YDiff = P.y - P2.y
                    Distance = math.sqrt((XDiff ** 2) + (YDiff ** 2))

                    if Distance < 10:
                        Distance = 10

                    #F = (G*M*M)/(R**2)
                    Force = 0.125 * (P.mass * P2.mass) / (Distance ** 2)
                    #F = M*A  ->  A = F/M
                    Acceleration = Force / P.mass
                    XComponent = XDiff / Distance
                    YComponent = YDiff / Distance
                    P.speedx -= Acceleration * XComponent
                    P.speedy -= Acceleration * YComponent

        for P in self.particles:
            P.x += P.speedx
            P.y += P.speedy

    def collision_detect(self):
        for P in self.particles:
            for P2 in self.particles:
                if P != P2:
                    Distance = \
                        math.sqrt(((P.x - P2.x) ** 2) + ((P.y - P2.y) ** 2))

                    if Distance < (P.radius + P2.radius):
                        P.speedx = \
                            ((P.mass * P.speedx) + (P2.mass * P2.speedx)) \
                            / (P.mass + P2.mass)
                        P.speedy = \
                            ((P.mass * P.speedy) + (P2.mass * P2.speedy)) \
                            / (P.mass + P2.mass)
                        P.x = ((P.mass * P.x) + (P2.mass * P2.x)) \
                            / (P.mass + P2.mass)
                        P.y = ((P.mass * P.y) + (P2.mass * P2.y)) \
                            / (P.mass + P2.mass)
                        P.mass += P2.mass
                        P.radius = math.sqrt(P.mass)
                        self.particles.remove(P2)

    def draw(self):
        self.Surface.fill((25, 0, 0))
        for P in self.particles:
            pygame.draw.circle(self.Surface,
                               (255, 255, 255),
                               (int(P.x),
                                int(600 - P.y)),
                               int(round(P.radius)))
        pygame.display.flip()

if __name__ == '__main__':
    game = Gravity(SCREEN_WIDTH, SCREEN_HEIGHT)
