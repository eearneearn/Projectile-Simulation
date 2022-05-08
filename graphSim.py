from pygame.locals import *
import pygame.math # for vector2
import math
from bullet import bulletSim

def showGraph(initialVelo,x,y):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1280,720)) #bg
    pygame.display.set_caption('The Amazing Circus: Projectile Simulation')
    done = False
    bulletShoot = bulletSim(initialVelo,x,y)

    while not done: # main game loop
        for event in pygame.event.get():
            if  event.type == QUIT:
                done = True
                pressed = pygame.key.get_pressed()
                        
        bulletShoot.update()
        bulletShoot.draw(DISPLAYSURF)
        pygame.display.update()   
    pygame.quit()  
