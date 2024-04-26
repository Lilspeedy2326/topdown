import pygame
import random

LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
Enemy = pygame.image.load('enemy.png') 
class enemy:
    def __init__(self):
        
        #player variables
        self.xpos = 800 #xpos of player
        self.ypos = 200 #ypos of player
        self.vx = 0 #x velocity of player
        self.vy = 0 #y velocity of player
        self.direction = RIGHT
         #ANIMATION VARIABLES VARIABLES
        self.frameWidth = 67
        self.frameHeight = 97
        self.RowNum = 1 #for down animation 
        self.frameNum = 0
        self.ticker= 0
        
    def draw(self,screen):
        pygame.draw.rect(screen, (0, 0, 251), (self.xpos, self.ypos, 30, 30))
        screen.blit(Enemy, (self.xpos, self.ypos), (self.frameWidth*self.frameNum, self.RowNum*self.frameHeight, self.frameWidth, self.frameHeight))
        
    def move(self,map, ticker, px, py):
        #randomly wander:
        if ticker % 40 == 0: #mess with this number to make him change direction more or less often!
            num = random.randrange(0, 4)
            if num == 0:
                self. direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = DOWN
            elif num == 3:
                self.direction = UP
            
        #check if player is direct line of sight
        if abs(int(py/50) - int(self.ypos/50))<2: #check that player and enmy are in same row
            if px < self.xpos: #check that player is to the left of enemy
                self.xpos-=5
                self.direction = LEFT
            else:
                self.xpos+=5
                self.direction = RIGHT
            
        if abs(int(py/50) - int(self.xpos/50))<2: #check that player and enmy are in same row
            if px < self.xpos: #check that player is to the left of enemy
                self.ypos+=5
                self.direction = DOWN
            else:
                self.ypos-=5
                self.direction = UP
                
        #check for collision and change direction if you've bumped
        if self.direction == RIGHT and map[int((self.ypos ) / 50)] [int( (self.xpos + 20) / 50)] ==2:
            #print("bumped right!")
            self.direction = LEFT
            self.xpos -= 6
        if self.direction == LEFT and map[int((self.ypos) / 50)] [int( (self.xpos - 20) / 50)] == 2:
            #print("bumped left!")
            self.direction = RIGHT
            self.ypos += 6
        if self.direction == DOWN and map[int((self.ypos + 20) / 50)] [int( (self.xpos) / 50)] ==2:
            #print("bumped down!")
            self.direction = UP
            self.ypos -= 6
        if self.direction == UP and map[int((self.ypos-20 ) / 50)] [int( (self.xpos) / 50)] == 2:
            #print("bumped UP!")
            self.direction = DOWN
            self.ypos += 6
            
        #or actually move!
        if self.direction == RIGHT:
            self.xpos += 3
        elif self.direction == LEFT:
            self.xpos -= 3
        elif self.direction == DOWN:
            self.ypos += 3
        elif self.direction == UP:
            self.ypos -= 3
        
        if self.vx != 0 or self.vy != 0: 
            ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          self.frameNum+=1
        if self.frameNum>3: 
           self.frameNum = 0
        print("framenum is", self.frameNum)
    
        

    
    
