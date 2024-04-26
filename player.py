import pygame

#CONSTANTS
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
man = pygame.image.load('symbiote_spiderman.png') # load your spritesheet
man.set_colorkey((255, 255, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

class player:
    def __init__(self):
        
        #player variables
        self.xpos = 400 #xpos of player
        self.ypos = 415 #ypos of player
        self.vx = 0 #x velocity of player
        self.vy = 0 #y velocity of player
        self.direction = LEFT
        #ANIMATION VARIABLES VARIABLES
        self.frameWidth = 64
        self.frameHeight = 96
        self.RowNum = 2 #for left animation
        self.RowNum = 3 #for right animation
        self.RowNum = 0 #for up animation
        self.RowNum = 1 #for down animation 
        self.frameNum = 0
        self.ticker= 0
        
    def draw(self,screen):
        #pygame.draw.rect(screen, (255, 0, 255), (self.xpos, self.ypos, 30, 30))
        screen.blit(man, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
    def move(self, keys, map):
        #LEFT MOVEMENT
        if keys[0] == True:
            self.vx = -3
            self.RowNum = 2
            self.direction = LEFT
            print("moving left")
        #RIGHT MOVEMENT
        elif keys[1] == True:
            self.vx = 3
            self.RowNum = 3
            self.direction = RIGHT
            print("moving right")
        #DOWN MOVEMENT
        
        # turn off x velcoity
        else:
            self.vx = 0
            
        self.xpos+=self.vx #updates player xpos
            
        if keys[2] == True:
            self.vy = 3
            self.RowNum = 0
            self.direction = DOWN
            print("moving down")
        #UP MOVEMENT
        elif keys[3] == True:
            self.vy = -3
            self.RowNum = 1
            self.direction = UP
            print("moving up")
        else:
            self.vy = 0
            
        self.ypos+=self.vy #updates player ypos
        #COLLISION
        #left collision
        if map[int((self.ypos- 10) / 50)][int((self.xpos) / 50)] == 2:
            self.xpos+=6
            
        #right collision
        if map[int((self.ypos-10) / 50)][int((self.xpos +30 +5) / 50)] == 2:
            self.xpos-=6
            
        #down collision
        if map[int((self.ypos +30 +5) / 50)][int((self.xpos) / 50)] == 2:
            self.ypos-=6
            
        #up collision
        if map[int((self.ypos-5) / 50)][int((self.xpos) / 50)] == 2:
            self.ypos+=6
            
        self.xpos+=self.vx #update player xpos
        self.ypos+=self.vy
            #ANIMATION------------------------------------------------------------------------------
        
        # only animate when in motion
        if self.vx != 0 or self.vy !=0: #animation
            #ticker is a spedometer. We don't want Man animating as fast as the
            #processor can process! Update Animation Frame each time ticker goes over
            self.ticker+=1
            if self.ticker%10==0: #only change frames every 10 ticks
                self.frameNum+=1
                #If we are over the number of framesin our sprite, reset to 0.
            if self.frameNum>3:
                self.frameNum = 0    
            

