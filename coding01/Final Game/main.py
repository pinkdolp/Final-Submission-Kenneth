# Yottie's Pong Game


# This below will import pygame and import the necessary other py files


import pygame
from paddle import Paddle
from ball import Ball
 
pygame.init()
 
#This will define colours
BLACK = (0,0,0)
WHITE = (255,255,255)
 
#New Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
#List of spirtes within the game 
all_sprites_list = pygame.sprite.Group()
 
# Adding paddles and the ball
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 

carryOn = True
 
#Screen Upadtes
clock = pygame.time.Clock()
 
#Initialise player scores
scoreA = 0
scoreB = 0
 
#This below is the main game loop
while carryOn:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Quit the game by pressing 'X'
                     carryOn=False
 
    #Paddle Control 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
    #Game Logic
    all_sprites_list.update()
    
    #If balls are bouncing against the walls
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    #Collision Detection
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    #Blank Screen
    screen.fill(BLACK)
    #The Net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    
    all_sprites_list.draw(screen) 
 
    #Showing the score
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
 
    #Screen Update
    pygame.display.flip()
     
    #Frame Rate
    clock.tick(60)
 

pygame.quit()