import pygame
import sys
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
# bgImg = os.path.join('/Users/aoomimkonnaiwaaa/Simulation Project/Projectile-Simulation/background-01.png')
# background = pygame.image.load(bgImg)
# DISPLAYSURF.blit(background, (1280,720))
#bgImg = pygame.image.load('/Users/aoomimkonnaiwaaa/Simulation Project/Projectile-Simulation/background-01.png')
DISPLAYSURF.blit(bgImg, (1280,720))

v0 = 5.536 
h = 0.2
alpha = 60
timestep = 0.005
gravity = -9.81
init_accel = pygame.Vector2(0,gravity)


#Calculation

init_vel = pygame.Vector2(math.cos(alpha*math.pi/180)*v0,math.sin(alpha * math.pi/180)*v0)
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

    pygame.draw.circle(DISPLAYSURF,(0,255,125), [50+pos.x*280,500-pos.y*112.5],4.5)
    pygame.display.update()

pygame.quit()