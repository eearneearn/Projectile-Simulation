import pygame
import sys
from pygame.locals import *
import pygame.math # for vector2
import math
import os
# import main
# import calculation

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1280,720))
pygame.display.set_caption('The Amazing Circus: Projectile Simulation')
done = False

#background
bgImg = pygame.image.load('background-01.png')
DISPLAYSURF.blit(bgImg,(0,0))

#shooter gun
bgImg = pygame.image.load('shooterGraph2.png')
DISPLAYSURF.blit(bgImg,(90,435))
# Set the size for the image
# DEFAULT_IMAGE_SIZE = (165.5, 163.5)
# Scale the image to your needed size
# bgImg = pygame.transform.scale(bgImg, DEFAULT_IMAGE_SIZE)

#goal
bgImg = pygame.image.load('goalNew.png')
DISPLAYSURF.blit(bgImg,(900,500))

#icon
shooterIcon = pygame.image.load('shooter.ico')
pygame.display.set_icon(shooterIcon)
 
v0 = 5.536 #initial velocity
h = 0.4 #sy from start
alpha = 60 #angle
timestep = 0.006
gravity = -9.81 #down
datum = -h
init_accel = pygame.Vector2(0,gravity)

#Calculation

init_vel = pygame.Vector2(math.cos(alpha * math.pi/180)*v0,math.sin(alpha * math.pi/180)*v0)
init_pos = pygame.Vector2(0,h) # x_axis,y_axis
pos = pygame.Vector2()
time = 0

while not done: # main game loop
    for event in pygame.event.get():
        if  event.type == QUIT:
            done = True
            pressed = pygame.key.get_pressed()
                       
    pos = init_pos + (init_vel * time) + ((1/2) * init_accel * time ** 2) # s = intialPostion + ut + (1/2at^2)
    time = time + timestep
    if pos.y >= - 0.9 : # บวกเพิ่ม - 0.7
        pygame.draw.circle(DISPLAYSURF,(255,255,255),[230 + pos.x * 280,490 - pos.y * 100],4.5) # y ต้องเป็นลบ เพราะทิศลง
    pygame.display.update()
    print(pos.y)
    

pygame.quit()