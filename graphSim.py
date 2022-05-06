import pygame
#import sys
from pygame.locals import *
import pygame.math
import math
import os
# import main
# import calculation

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280,720))
pygame.display.set_caption('The Amazing Circus')
done = False
#background
bgImg = pygame.image.load('background-01.png')
DISPLAYSURF.blit(bgImg,(0,0))
#shooter gun
bgImg = pygame.image.load('shooterGraph.png')
DISPLAYSURF.blit(bgImg,(50,400))
# Set the size for the image
# DEFAULT_IMAGE_SIZE = (165.5, 163.5)
# Scale the image to your needed size
# bgImg = pygame.transform.scale(bgImg, DEFAULT_IMAGE_SIZE)
#goal
bgImg = pygame.image.load('goal.png')
DISPLAYSURF.blit(bgImg,(990,570))
shooterIcon = pygame.image.load('shooter.ico')
pygame.display.set_icon(shooterIcon)
 

v0 = 5.536 
h = 0.2
alpha = 60
timestep = 0.006
gravity = -9.81
init_accel = pygame.Vector2(0,gravity)


#Calculation

init_vel = pygame.Vector2(math.cos(alpha * math.pi/180)*v0,math.sin(alpha * math.pi/180)*v0)
init_pos = pygame.Vector2(0,h)
pos = pygame.Vector2()
time = 0

while not done: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
            pressed = pygame.key.get_pressed()

    pos = init_pos + init_vel * time + init_accel * time * time * 0.5
    time += timestep

    pygame.draw.circle(DISPLAYSURF,(255,255,255), [230+pos.x*280,520-pos.y*100],4.5)
    pygame.display.update()

pygame.quit()