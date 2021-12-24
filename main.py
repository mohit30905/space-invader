#space
import pygame
import random
import math
from pygame import mixer
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("space(rupesh)")
running=True
background=pygame.image.load("background.png")

score=0
font=pygame.font.Font("freesansbold.ttf",32)
font1=pygame.font.Font("freesansbold.ttf",40)
#loading ufo
ufo=pygame.image.load("ufo.png")
ufo_x=400
ufo_y=534
ufo_dx=0
ufo_dy=0
#bullet
bu=pygame.image.load("bullet.png")
state="rest"
bullet_x=ufo_x
bullet_y=524
n=3
clock = pygame.time.Clock()

def player(x,y):
    screen.blit(ufo,(x,y))
def enemy(x,y,i):
    screen.blit(en[i],(x,y))
def bullet(x,y):
    global state
    state="fire"
    screen.blit(bu,(x+10,y-10))
#loading enemies
def isCollision(en_X, en_Y, bullet_X, bullet_Y):
    distance = math.sqrt(math.pow(en_X - bullet_X, 2) + (math.pow(en_Y - bullet_Y, 2)))
    if distance < 35:
        return True
    else:
        return False
def show_score(x=10,y=10):
    s=font.render("SCORE :"+str(score), True,(255,255,255))
    screen.blit(s,(x,y))
    s1=font.render("......................................................................................", True,(255,255,255))
    screen.blit(s1,(0,500))
    
    
def game_over():
    for i in range(n):
        en_y[i]=2000
    s=font1.render("GAME OVER", True,(255,255,255))
    screen.blit(s,(245,200))
    

    

en=[]
en_x=[]
en_y=[]
x_change=[]
y_change=[]
a=[7,-7]

for i in range(n):
    en.append(pygame.image.load("enemy.png"))
    en_x.append(random.randint(0,734))
    en_y.append(random.randint(64,150))
    x_change.append(a[random.randint(0,1)])
    y_change.append(50)  
    enemy(en_x[i],en_y[i],i)

while running:
    screen.blit(background, (0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                ufo_dx=-6
            if event.key== pygame.K_RIGHT:
                ufo_dx=6
            if event.key== pygame.K_UP:
                ufo_dy=-6
            if event.key== pygame.K_DOWN:
                ufo_dy=+6
            if event.key==pygame.K_SPACE:
                bullet_x=ufo_x
                bullet_y=ufo_y
                bullet(bullet_x,bullet_y)
        
                
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ufo_dx = 0 
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ufo_dy = 0    
            
                
    ufo_x=ufo_x+ufo_dx  
    ufo_y=ufo_y+ufo_dy
    
    if ufo_x>=734:
        ufo_x=734
    if ufo_x<=0:
        ufo_x=0
    if ufo_y<=300:
        ufo_y=300
    if ufo_y>=534:
        ufo_y=534
    
    #enemy movement
       
    for i in range(n):
        #collosion
        if isCollision(en_x[i], en_y[i], bullet_x, bullet_y):
            state="rest"
            bullet_y=ufo_y-10
            en_x[i]=random.randint(0,734)
            en_y[i]=random.randint(64,150)
            score+=1
            if score%5==0:
                n+=1
                en.append(pygame.image.load("enemy.png"))
                en_x.append(random.randint(0,734))
                en_y.append(random.randint(64,150))
                x_change.append(a[random.randint(0,1)])
                y_change.append(50)  
                enemy(en_x[i],en_y[i],i)
                
            
            
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()            
        
        en_x[i]=en_x[i]+x_change[i]
        enemy(en_x[i],en_y[i],i)
       
        if en_x[i]>=735:
            en_y[i]+=y_change[i]
            x_change[i]=-7   
        if en_x[i]<=0:
            en_y[i]+=y_change[i]
            x_change[i]=7
    #bullet movment
    if state== "fire":
        bullet(bullet_x,bullet_y) 
        bullet_y=bullet_y-12
    if bullet_y<=-25:
        bullet_y=534
        state="rest"
    #game_over
    for i in en_y:
        if i>=480:
            game_over()
            
    
    show_score()           
    player(ufo_x,ufo_y)
    pygame.display.update()
    clock.tick(60)
    if not running:
        pygame.display.quit()
