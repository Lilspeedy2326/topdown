import pygame
from player import player
from fireball import fireball
from enemy import enemy 
pygame.init()
pygame.font.init() # you have to call this at the start, if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("top down grid game") # sets the window title
screen = pygame.display.set_mode((1000,800)) # creates game screen
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop


# player variables
xpos= 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
button2 = False
button3 = False
#add more buttons here!
quitGame = False

#CONSTANTS
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5
ticker = 0
#instantiate a player
p1 = player()

ball = fireball()

e1 = enemy()

keys = [False, False, False, False, False]
map = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
       [2,1,1,1,1,1,1,1,1,2,3,2,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,2,3,2,3,2,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1,2],
       [2,1,2,3,2,1,1,1,1,1,1,1,1,2,3,2,3,2,1,2],
       [2,1,2,2,2,1,1,1,1,1,1,1,1,2,2,3,2,2,1,2],
       [2,1,2,3,2,1,1,1,1,1,1,1,1,2,3,2,3,2,1,2],
       [2,1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,1,2],
       [2,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
       [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
       
brick = pygame.image.load('brick.png')
dirt = pygame.image.load('dirt.png')
water = pygame.image.load('water.png')
open_screen_text = my_font.render('Gerardo\'s Adventure', False, (0, 0, 0))
#have more of these for other text blocks
 
while not gameover:#GAME LOOP=========================================================================================
    clock.tick(60) #FPS
    ticker += 1
    #input section--------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            if event.key == pygame.K_SPACE:
                keys[SPACE] = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            if event.key == pygame.K_SPACE:
                keys[SPACE] = False
                
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False
   
    #physics section------------------------------------------------------------------
    p1.move(keys, map)
    e1.move(map, ticker, p1.xpos, p1.ypos)
    ball.move()
    #check space for shooting
    if keys[SPACE] == True:
        ball.shoot(p1.xpos, p1.ypos, p1.direction)
        
    print(mousePos)#uncomment for testing
    
    #state 1: menu state!------------------------------
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
        
    if state == 1 and mousePos[0]>400 and mousePos[0]<600 and mousePos[1]>400 and mousePos[1]<600:
        button2 = True
    else:
        button2 = False
        
    if state == 1 and mousePos[0]>700 and mousePos[0]<898 and mousePos[1]>400 and mousePos[1]<600:
        button3 = True
    else:
        button3 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    
    if state == 1 and button2 == True and mouseDown == True:
        state = 3
        
    if state == 1 and button3 == True and mouseDown == True:
        state = 4
    #state 2: playing state!---------------------------
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 3 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    if state == 4 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    #regular game physics would go here

    #render section-------------------------------------------------------------------------        
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    #draw map
    
        
    #menu state-------------------------------
    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink
        screen.blit(open_screen_text, (100,100))
        #have more text here for buttons and whatnot
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150)) #dark green            
        else:
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))#light green
            
        if button2 == False:
            pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (400, 400, 200, 150))
            
        #repeat for third button
        if button3 == False:
            pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (700, 400, 200, 150))
    
    #game state-------------------------------
    if state == 2:
        screen.fill((80,150,100))# Clear the screen green
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                   screen.blit(dirt, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 2:
                    screen.blit(brick, (j * 50, i * 50), (0, 0, 50, 50))
                if map[i][j] == 3:
                    screen.blit(water, (j * 50, i * 50), (0, 0, 50, 50))
        p1.draw(screen)
    
        if ball.isAlive == True:
            ball.draw(screen)
            
        e1.draw(screen)
        
    #if state == 3:
        #screen.fill((64,224,208))# clear the screen turquoise
        
    #if state == 4:
        #screen.fill((139,0,0))#clear the screen darkred
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop=========================================================================================================
pygame.quit()

