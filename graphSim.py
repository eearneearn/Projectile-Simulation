from pygame.locals import *
import pygame.math # for vector2
import math
from bullet import bulletSim

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280,720)) #bg
pygame.display.set_caption('The Amazing Circus: Projectile Simulation')
done = False
bulletShoot = bulletSim(position.x,position.y,initialVelo,angle,timestep)
ิbulletShootList = [bulletShoot]

while not done: # main game loop
    for event in pygame.event.get():
        if  event.type == QUIT:
            done = True
            pressed = pygame.key.get_pressed()
                       
    for i in range(len(bulletShoot)):
        bulletShoot.update()
        bulletShoot[i].draw(DISPLAYSURF)
    pygame.display.update()   
   
pygame.quit()  