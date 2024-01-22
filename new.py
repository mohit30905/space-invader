import pygame
import random
import time
import math

from userBot1 import run as bot1
from userBot2 import run as bot2

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Zine Algo Pseudo")

# Set up the game variables
running = True
background = pygame.image.load("background.png")
score1 = 0
score2=0
font = pygame.font.Font(None, 32)
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 24)


# Load UFO images
ufo = pygame.image.load("ufo.png")
ufo2 = pygame.image.load("ufo.png")
ufo2 = pygame.transform.rotate(ufo2, 180)

# Load bullet images
bu = pygame.image.load("bullet.png")
bu2 = pygame.transform.rotate(bu, 180)  # Rotate bullet image for player 2

# UFO properties
ufo_x = 734
ufo_y = 534
ufo_dx = 0
ufo_dy = 0

ufo2_x = 0
ufo2_y = 66
ufo2_dx = 0
ufo2_dy = 0

# Bullet properties
bullet_x = ufo_x
bullet_y = 524
state_player1 = "rest"

bullet2_x = ufo2_x
bullet2_y = 76
state_player2 = "rest"

bullet1_count = 20
bullet2_count = 20


t=time.time()

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to draw the player
def player(x, y):
    screen.blit(ufo, (x, y))

def player2(x, y):
    screen.blit(ufo2, (x, y))

# Function to draw bullets
def bullet(x, y):
    global state_player1
    state_player1 = "fire"
    screen.blit(bu, (x + 10, y - 10))

def bullet2(x, y):
    global state_player2
    state_player2 = "fire"
    screen.blit(bu2, (x + 10, y + 10))

# Collision check
def isCollision(en_X, en_Y, bullet_X, bullet_Y):
    distance = math.sqrt(math.pow(en_X - bullet_X, 2) + (math.pow(en_Y - bullet_Y, 2)))
    if distance < 35:
        return True
    else:
        return False
    
    


# Function to display score
def show_score(x=10, y=10):
    s1 = font.render("SCORE 1: " + str(score1), True, (255, 255, 255))
    s4 = font2.render("Bullets Left: " + str(bullet1_count), True, (255, 255, 255))

    s2 = font.render("SCORE 2: " + str(score2), True, (255, 255, 255))
    s5 = font2.render("Bullets Left: " + str(bullet2_count), True, (255, 255, 255))

    s3 = font.render("Timer " + '%.2d' % (time.time()-t) , True, (255, 255, 255))
    screen.blit(s1, (x, y))
    screen.blit(s4, (10, 40))

    screen.blit(s2, (650,10))
    screen.blit(s5, (650, 40))

    screen.blit(s3, (350,10))

    # s1 = font.render("......................................................................................",
    #                 True, (255, 255, 255))
    # screen.blit(s1, (0, 500))
    # screen.blit(s2, (0, 500))

# Function to display game over message
def game_over():

    s = font1.render("GAME OVER", True, (255, 255, 255))
    w="TIE"
    if score1>score2:
        w="Player 1 wins"
    elif score2>score1:
        w="Player 2 wins"
    s = font.render(w, True, (255, 255, 255))
    # p = s.get_rect(center=)
    screen.blit(s, (350, 300))



# Main game loop
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                ufo_x = 734
                ufo_y = 534
                ufo_dx = 0
                ufo_dy = 0

                ufo2_x = 0
                ufo2_y = 66
                ufo2_dx = 0
                ufo2_dy = 0

                # Bullet properties
                bullet_x = ufo_x
                bullet_y = 524
                state_player1 = "rest"

                bullet2_x = ufo2_x
                bullet2_y = 76
                state_player2 = "rest"
                t=time.time()
                 

                
 
    if(time.time()-t>20 or score1>=10 or score2>=10 ):
        game_over()
        pygame.display.update()
        clock.tick(60)
        continue
        

   
    p1input,shoot1=bot1(bullet2_x,bullet2_y,ufo_x,ufo_y,ufo2_x,ufo2_y,state_player1,state_player2, bullet1_count)
    p2input,shoot2=bot2(bullet_x,bullet_y,ufo2_x,ufo2_y,ufo_x,ufo_y,state_player2,state_player1, bullet2_count)
    # Player 1 controls
    if p1input.lower()=="left":
        ufo_dx = -6
    if  p1input.lower()=="right":
        ufo_dx = 6
    if shoot1:
        if state_player1 == "rest" and bullet1_count > 0:
            bullet_x = ufo_x
            bullet_y = ufo_y
            bullet1_count -= 1
            bullet(bullet_x, bullet_y)

    if p2input.lower()=="left":
        ufo2_dx = -6
    if  p2input.lower()=="right":
        ufo2_dx = 6
    if shoot2:
        if state_player2 == "rest" and bullet2_count > 0:
            bullet2_x = ufo2_x
            bullet2_y = ufo2_y
            bullet2_count -= 1

            bullet2(bullet2_x, bullet2_y)

    # Update player 1 position
    ufo_x = ufo_x + ufo_dx
    ufo_y = ufo_y + ufo_dy

    # Ensure player 1 stays within bounds
    if ufo_x >= 734:
        ufo_x = 734
    if ufo_x <= 0:
        ufo_x = 0
    if ufo_y <= 300:
        ufo_y = 300
    if ufo_y >= 534:
        ufo_y = 534

    # Update player 2 position
    ufo2_x = ufo2_x + ufo2_dx
    ufo2_y = ufo2_y + ufo2_dy

    # Ensure player 2 stays within bounds
    if ufo2_x >= 734:
        ufo2_x = 734
    if ufo2_x <= 0:
        ufo2_x = 0
    if ufo2_y <= 0:
        ufo2_y = 0
    if ufo2_y >= 266:
        ufo2_y = 266

    # Handle bullets for player 1
    if state_player1 == "fire":
        bullet(bullet_x, bullet_y)
        bullet_y = bullet_y - 12

    if bullet_y <= -25:
        bullet_y = 534
        state_player1 = "rest"

    # Handle bullets for player 2
    if state_player2 == "fire":
        bullet2(bullet2_x, bullet2_y)
        bullet2_y = bullet2_y + 12

    if bullet2_y >= 600:
        bullet2_y = 76
        state_player2 = "rest"

 
  

    # Check for collisions between bullets and player 2
    if isCollision(ufo2_x,ufo2_y, bullet_x, bullet_y,):
        state_player1 = "rest"
        bullet_y = ufo_y - 10
        score1 += 1
    if isCollision(ufo_x,ufo_y, bullet2_x, bullet2_y):
        state_player2 = "rest"
        bullet2_y = ufo2_y - 10
        score2 += 1


 

    show_score()
    player(ufo_x, ufo_y)
    player2(ufo2_x, ufo2_y)
    pygame.display.update()


    clock.tick(60)

    if not running :
        pygame.display.quit()
