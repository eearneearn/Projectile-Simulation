from pygame.locals import *
import pygame.math # for vector2
import math
from bullet import bulletSim

def showGraph(initialVelo,y): 
    pygame.init()
    #background
    DISPLAYSURF = pygame.display.set_mode((1280,720)) #bg
    pygame.display.set_caption('The Amazing Circus: Projectile Simulation')    
    bgImg = pygame.image.load('background-01.png')
    DISPLAYSURF.blit(bgImg,(0,0))
    #shooter gun
    bgImg = pygame.image.load('shooterGraph2.png')
    DISPLAYSURF.blit(bgImg,(90,433))
    # Set the size for the image
    # DEFAULT_IMAGE_SIZE = (165.5, 163.5)
    # Scale the image to your needed size
    # bgImg = pygame.transform.scale(bgImg, DEFAULT_IMAGE_SIZE)

    #goal
    bgImg = pygame.image.load('goalNew.png')
    DISPLAYSURF.blit(bgImg,(900,530))

    #icon
    shooterIcon = pygame.image.load('shooter.ico')
    pygame.display.set_icon(shooterIcon)
    
    done = False
    bulletShoot = bulletSim(initialVelo,y)
   
    while not done: # main game loop
        for event in pygame.event.get():
            if  event.type == QUIT:
                done = True
                #pressed = pygame.key.get_pressed()
                        
        bulletShoot.update()
        bulletShoot.draw(DISPLAYSURF)
        pygame.display.update()   
    pygame.quit()  

showGraph(5.536, 0.2) 