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
<<<<<<< HEAD
from pygame.locals import *

FRAME_RATE = 60

clock = pygame.time.Clock()

pygame.init()

#The bit that asks you questions

#how many particles do you want?
while True:
    ParticleNumber = raw_input("Enter how many particles to draw: ")
    try:
        ParticleNumber = int(ParticleNumber)
        break
    except:
        print "\nWell, now.  Let's try that again."

#How big do you want the screen?
while True:        
    Screenx = raw_input ("Enter Screen Width: ")
    try:
        Screenx = int(Screenx)
        break
    except:
        print "\nWell, now.  Let's try that again."
        
while True:
    Screeny = raw_input ("Enter Screen Height: ")
    try:
        Screeny = int(Screeny)
        break
    except:
        print "\nWell, now.  Let's try that again."

#how big do you want to make the Central Particle
while True:
    CentreMass = raw_input ("Enter Central Particle Mass (0 = No Centre): ")
    try:
        CentreMass = int(CentreMass)
        break
    except:
        print "\nWell, now.  Let's try that again."
=======

from pygame.locals import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
>>>>>>> 5760df3fc3eb6231a058857ea9fefbdc0c93242d

# how fast do you want the particles?
ParticleVelocity = input ("Enter Max Particle Velocity: ") 

<<<<<<< HEAD
#The bit that that makes the screen
Surface = pygame.display.set_mode((Screenx, Screeny))

#The bit that makes the particles work
Particles = []
=======
>>>>>>> 5760df3fc3eb6231a058857ea9fefbdc0c93242d
class Particle:
    def __init__(self, x, y, speedx, speedy, mass):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.mass = mass
        self.radius = math.sqrt(self.mass)

<<<<<<< HEAD
#The big Central Particle
if CentreMass > 0:
    Particles.append(Particle(Screenx/2, Screeny/2, 0.0, 0.0, CentreMass))
#The little particles
for x in range(ParticleNumber):
    Particles.append(Particle(random.randint(10,Screenx - 10), random.randint(10,Screeny - 10), random.uniform(-ParticleVelocity, ParticleVelocity), random.uniform(-ParticleVelocity, ParticleVelocity), random.uniform(1, 10)))
    
#The bit that figures out the complex gravity stuff.
def Move():
    for P in Particles:
        for P2 in Particles:
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

    for P in Particles:
        P.x += P.speedx
        P.y += P.speedy

#The bit that detects collisions (Duh.)
def CollisionDetect():
    for P in Particles:
        for P2 in Particles:
            if P != P2:
                Distance = math.sqrt(((P.x - P2.x) ** 2) + ((P.y - P2.y) ** 2))
                if Distance < (P.radius + P2.radius):
                    P.speedx = ((P.mass * P.speedx) + (P2.mass * P2.speedx)) \
                        / (P.mass + P2.mass)
                    P.speedy = ((P.mass * P.speedy) + (P2.mass * P2.speedy)) \
                        / (P.mass + P2.mass)
                    P.x = ((P.mass * P.x) + (P2.mass * P2.x)) \
                        / (P.mass + P2.mass)
                    P.y = ((P.mass * P.y) + (P2.mass * P2.y)) \
                        / (P.mass + P2.mass)
                    P.mass += P2.mass
                    P.radius = math.sqrt(P.mass)
                    Particles.remove(P2)

#The bit that draws up the screen and the dots
def Draw():
    Surface.fill((0, 0, 0))
    for P in Particles:
        pygame.draw.circle(Surface,
                           (255, 255, 255),
                           (int(P.x),
                           int(600 - P.y)),
                           int(round(P.radius)))
##        Surface.set_at((int(P.x),int(600-P.y)),(255,255,255))
    pygame.display.flip()

# The bit that lets it quit
def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit()
            sys.exit()

#The bit that makes it actually run
def main():
    while True:
        # Limiting Frame Rate to 50 fps
        time_passed = clock.tick(FRAME_RATE)
        
        GetInput()
        Move()
        CollisionDetect()
        Draw()
=======

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
>>>>>>> 5760df3fc3eb6231a058857ea9fefbdc0c93242d

if __name__ == '__main__':
    game = Gravity(SCREEN_WIDTH, SCREEN_HEIGHT)
