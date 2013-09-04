import pygame
import random
import math
import sys
from pygame.locals import *

FRAME_RATE = 60

clock = pygame.time.Clock()

pygame.init()

while True:
    ParticleNumber = raw_input("Enter how many particles to draw: ")
    try:
        ParticleNumber = int(ParticleNumber)
        break
    except:
        print "\nWell, now.  Let's try that again."
        
while True:        
    Screenx = raw_input ("Enter Screen Height:")
    try:
        Screenx = int(Screenx)
        break
    except:
        print "\nWell, now.  Let's try that again."
        
while True:
    Screeny = raw_input ("Enter Screen Width:")
    try:
        Screeny = int(Screeny)
        break
    except:
        print "\nWell, now.  Let's try that again."

Screen_Size = (Screenx, Screeny)
Surface = pygame.display.set_mode((Screenx, Screeny))

Particles = []


Particles = []
class Particle:
    def __init__(self, x, y, speedx, speedy, mass):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.mass = mass
        self.radius = math.sqrt(self.mass)

Particles.append(Particle(Screenx/2, Screeny/2, 0.0, 0.0, 1000))

for x in range(ParticleNumber):
    Particles.append(Particle(random.randint(10,Screenx - 10), random.randint(10,Screeny - 10), random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5), random.uniform(1, 10)))
    

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


def Draw():
    Surface.fill((25, 0, 0))
    for P in Particles:
        pygame.draw.circle(Surface,
                           (255, 255, 255),
                           (int(P.x),
                           int(600 - P.y)),
                           int(round(P.radius)))
##        Surface.set_at((int(P.x),int(600-P.y)),(255,255,255))
    pygame.display.flip()


def GetInput():
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit()
            sys.exit()


def main():
    while True:
        # Limiting Frame Rate to 50 fps
        time_passed = clock.tick(FRAME_RATE)
        
        GetInput()
        Move()
        CollisionDetect()
        Draw()

if __name__ == '__main__':
    main()
