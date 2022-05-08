from pygame.locals import *
import pygame.math # for vector2
import math
# import main

class bulletSim:
    def __init__(self,initialVelo,y):
        self.timestep = 0.006
        self.time = 0
        self.initialAccel = pygame.Vector2(0,-9.81) #down
        self.initialVelo2 = pygame.Vector2(math.cos(60 * math.pi/180)*initialVelo,math.sin(60 * math.pi/180)*initialVelo)
        self.initialPost = pygame.Vector2(0,y) # x_axis,y_axis
        self.position = pygame.Vector2() # x_axis,y_axis
    
    def draw(self,surface):
        pygame.draw.circle(surface,(38,255,0),[245 + self.position.x * 280,510 - self.position.y * 165],4.5) # y ต้องเป็นลบ เพราะทิศลง
    
    def update(self):
        if self.position.y >= - 0.2 : 
            self.position = self.initialPost + (self.initialVelo2 * self.time) + ((1/2) * self.initialAccel * self.time ** 2) # s = intialPostion + ut + (1/2at^2)
            self.time = self.time + self.timestep 
            
                        
# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((1280,720))
# pygame.display.set_caption('The Amazing Circus: Projectile Simulation')
# done = False

# #background
# bgImg = pygame.image.load('background-01.png')
# DISPLAYSURF.blit(bgImg,(0,0))

# #shooter gun
# bgImg = pygame.image.load('shooterGraph2.png')
# DISPLAYSURF.blit(bgImg,(90,433))
# # Set the size for the image
# # DEFAULT_IMAGE_SIZE = (165.5, 163.5)
# # Scale the image to your needed size
# # bgImg = pygame.transform.scale(bgImg, DEFAULT_IMAGE_SIZE)

# #goal
# bgImg = pygame.image.load('goalNew.png')
# DISPLAYSURF.blit(bgImg,(900,530))

# #icon
# shooterIcon = pygame.image.load('shooter.ico')
# pygame.display.set_icon(shooterIcon)
 
# v0 = 5.536 #initial velocity
# h = 0 #sy from start
# alpha = 60 #angle
# timestep = 0.006
# gravity = -9.81 #down
# initialAccel = pygame.Vector2(0,gravity)

# #Calculation

# initialVelo2 = pygame.Vector2(math.cos(alpha * math.pi/180)*v0,math.sin(alpha * math.pi/180)*v0)
# initialPost = pygame.Vector2(0,h) # x_axis,y_axis
# position = pygame.Vector2()
# time = 0

# while not done: # main game loop
#     for event in pygame.event.get():
#         if  event.type == QUIT:
#             done = True
#             pressed = pygame.key.get_pressed()
                       
   
#     if position.y >= - 0.2 : 
#         position = initialPost + (initialVelo2 * time) + ((1/2) * initialAccel * time ** 2) # s = intialPostion + ut + (1/2at^2)
#         time = time + timestep
#         pygame.draw.circle(DISPLAYSURF,(38,255,0),[250 + position.x * 280,500 - position.y * 150],4.5) # y ต้องเป็นลบ เพราะทิศลง
#     pygame.display.update()
#     #print(pos.y)
    

# pygame.quit()