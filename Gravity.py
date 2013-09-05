#     ___     ____       _     _     _   _____   _______  __ __
#   /|       ||  \\    // \\   \\   //   I===I   |I---I|  \\ //
#   ||   __  ||==//   ||===||   \\ //     |||      |||     \Y/
#   \|___|/  ||  \\   ||   ||    \v/     I===I     |||     |||
#
#   A little program that creates little simulation of gravity 
#   a little solar system. The original program, which did all
#   the actual "Gravity Simulating" was written by Ian Mallet.
#                             Enjoy it!
#   "I've always thought that one of the the great things about
#    physics is that you can add more digits to any number and
#          see what happens and nobody can stop you."
#    -- Randall Monroe

import pygame
import random
import math
import sys

from pygame.locals import *

while True:
    SCREEN_WIDTH = raw_input("Enter screen width: ")
    # Make sure the number supplied is an int otherwise ask again.
    try:
        SCREEN_WIDTH = int(SCREEN_WIDTH)
        break
    except:
        print "\nWell, now.  Let's try that again."

while True:
    SCREEN_HEIGHT = raw_input("Enter screen height: ")
    # Make sure the number supplied is an int otherwise ask again.
    try:
        SCREEN_HEIGHT = int(SCREEN_HEIGHT)
        break
    except:
        print "\nWell, now.  Let's try that again."
            
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

        ParticleVelocity = input("Enter particle max speed: ")
            
        while True:
            CentreSize = raw_input("Enter how large the central particle is: ")
            # Make sure the number supplied is an int otherwise ask again.
            try:
                CentreSize = int(CentreSize)
                break
            except:
                print "\nWell, now.  Let's try that again."

        # Create a large particle in the center of the system
        self.particles.append(Particle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0.0, 0.0, CentreSize))

        # Create some random little particles.
        for x in range(ParticleNumber):
            self.particles.append(Particle(random.randint(10, SCREEN_WIDTH - 10),
                                           random.randint(10, SCREEN_HEIGHT - 10),
                                           random.uniform(-ParticleVelocity, ParticleVelocity),
                                           random.uniform(-ParticleVelocity, ParticleVelocity),
                                           random.randint(1, 10)))

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
