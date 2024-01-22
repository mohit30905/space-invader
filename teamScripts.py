import random

#no name
def noname(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right']
  i = random.randrange(0, 2)
  move = directions[i]
  shoot = random.randrange(0, 2)
  if enemyState==0:
    if playerX==enemyX:
      return move, shoot
  if enemyState==1:
    if playerX==enemyX:
      return move, shoot
  return move, shoot

#codemasters
def codemasters(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right','none']
  # i = random.randrange(0, 2)
  # move = directions[i]
 # shoot = random.randrange(0, 2)
  move="left"
  shoot=0
  if enemyX-playerX<0.9 and bulletX!=enemyX:
    move="none"
    shoot=1
   
  elif enemyX-playerX==0 and bulletX!=enemyX:
    move="none"
    shoot=1
 
  elif enemyX-playerX<0 and bulletX==playerX and enemyState=="true" and bulletY-enemyY>0:
    move="right"
    shoot=0
  elif enemyX-playerX<0 and bulletX==playerX and enemyState=="true":
    move="left"
    shoot=0
   
  elif enemyX-playerX>0 and enemyState =="true":
    move="left"
    shoot=0

  elif enemyX-playerX>0 and enemyState =="false":
    move="right"
    shoot=0
 
  elif enemyX-playerX<0 and enemyState=="true":
    move="right"
    shoot=0
   
  elif enemyX-playerX<0 and enemyState=="false":
    move="left"
    shoot=0
  return move,shoot

#hecker
def hecker(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right']
  i = random.randrange(0, 2)
  move = directions[i]
  shoot = random.randrange(0, 2)
  defensive = True

  enemybcount = 20

  if(bulletY != 0 and bulletThrown == 0):
    bulletThrown = 1
    enemybcount = enemybcount - 1
   

  if(bulletY ==0 and bulletThrown == 1):
    bulletThrown = 0  
  if(bulletCount == 0):
    defensive = False

   
  if( abs(bulletX-playerX) < 20 and (abs(bulletY-playerY) < 30)): #defENSIVE!

    if(playerX <10):
      return directions[1], False
   
    return directions[0], False

  if(defensive):
    return random.randrange(0,1), False


  if(playerX == enemyX):
    return directions[2], True
  
#crocin
def crocin(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right','none']
  playerState = ['ready','fire']
  playerX = 400
  #i = random.randrange(0, 2)  shoot = [0,1]
  y = bulletY-playerY
  x = bulletX - playerX
  if x==0:
    if y<=200 :
      if playerX ==0:
        move = directions[1]
        if playerX == 0:
            move  = directions[0]
        else:
            pass
      elif playerX == 800:
        move = directions[0]
        if playerX == 800:
            move = directions[1]
        else:
            pass
      else:
        move = directions[random.randrange(0, 2)]
  else :
    move = directions[2]
  distanceX = enemyX - playerX
  if distanceX<=100:
    shoot = True
  else:
    shoot = False
  return move, shoot

#random
def teamrandom(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right']
  i = random.randrange(0, 2)
  move = directions[i]
  shoot = random.randrange(0, 2)
  if shoot==1:
    bulletCount+=1
  if move=='left':
    playerX-=1
  elif move=='right':
    playerX+=1
  if playerX<0:
    playerX=0
  elif playerX>600:
    playerX=600
  if playerY<0:
    playerY=0
  elif playerY>800:
    playerY=800
  if bulletCount>0:
    bulletX+=1
  if bulletX>600:
    bulletX=600
  if bulletX==enemyX and bulletY==enemyY:
    bulletCount-=1
  if bulletCount>0:
    bulletY+=1
  if bulletY>800:
    bulletY=80
  if bulletY==playerY and bulletX==playerX:  
    if bulletX==playerX and bulletY==playerY:
        bulletCount-=1
  if bulletCount>0:
    enemyX-=1
  if enemyX<0:
    enemyX=0
  elif enemyX>600:
    enemyX=600
  if bulletCount>0:
    bulletY-=1
    if enemyY<0:
      enemyY=0
    elif enemyY>800:
      enemyY=800
  if bulletCount>0:
    if playerX==bulletX and playerY==bulletY:
      playerState='dead'
  if bulletCount>0:
    if enemyX==bulletX and enemyY==bulletY:
      enemyState='dead'
  return playerX,playerY,enemyX,enemyY,bulletCount,playerState,enemyState,bulletX,bulletY

  return move, shoot

#starboss
def starboss(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions =["Left ","Right"]
  while(True):
   if(bulletX<playerX):
     move=directions[1]
   elif(bulletX>playerX):
     move=directions[0]
   elif(bulletX==playerX):
      directions = ['left', 'right']
      i = random.randrange(0, 2)
      move = directions[i]
   if (playerX<enemyX):
      move=directions[1]
   elif (playerX>enemyX):
      move=directions[0]
   elif (playerX==enemyX):
      shoot=True
      directions = ['left', 'right']
      i = random.randrange(0, 2)
      move = directions[i]
      if(playerX==0):
        move=directions[1]
      elif(playerX==600):
        move=directions[0]

#helloworld
def helloworld(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount, shoot, move):
  if( enemyState == True):
    if( bulletX==playerX):
      if( enemyX==bulletX):
        n = random.randrange(0,2)
        if( n==0):
          move = "left"
        else:
          move = "right"
      else:
        if( enemyX>playerX):
          while( enemyX>playerX):
            move = "right"  
            playerX = playerX+1
          if( bulletCount>0):
            if( playerState == False):
              playerState = True

        else:
          while( enemyX<playerX):
            move = "left"
            playerX = playerX-1
          if( bulletCount>0):
            if( playerState == False):
              playerState = True
    else:
      #if( enemyX == bulletX) stay in the same position
      if( enemyX!=bulletX):
        if( enemyX>playerX):
          while( enemyX>playerX):
            if( playerX == bulletX):
              break
            else:
              move = "right"  
              playerX = playerX+1
          if( bulletCount>0):
            if( playerState == False):
              playerState = True
        else:
          while( playerX>enemyX):
            if( playerX==bulletX):
              break
            else:
              move = "left"
              playerX = playerX-1
          if( bulletCount>0):
            if( playerState == False):
              playerState = True
  else:
    if( enemyX==playerX):
      if( bulletCount<20):
        if( playerState==False):
          playerState=True
    else:
      if( enemyX<playerX):
        while( enemyX<playerX):
          move="left"
          playerX=playerX-1
        if( bulletCount<20):
          if( playerState==False):
            playerState=True
      else:    
        while( enemyX>playerX):
          move="right"
          playerX=playerX+1
        if( bulletCount<20):
          if( playerState==False):
            playerState=True
  if( playerState == True):
    shoot = True
  else:
    shoot = False
   
       
  return (move, shoot)

#rocket
def rocket(bulletX,bulletY,playerX,playerY,enemyX,enemyY,
        playerState,enemyState, bulletCount):
  directions = ['left', 'right','none']
  shoot = 0
  if(playerX>enemyX) :
    i = 0
  elif(playerX<enemyX) :
    i = 1
  else :
    i = 2
  move = directions[i]
  if(playerX-enemyX<200 | playerX-enemyX>-200):
   shoot = 1
  while (bulletX==playerX & (bulletY-playerY)<200):
    if(playerX!=0):
      move = 'left'
    else:
      move = 'right'
  return move, shoot

#coderangers
import random
def coderangers(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right']
  i = random.randrange(0, 2)
  move = directions[i]
  shoot = random.randrange(0, 2)

  if (playerX>enemyX):
   move = 'left'
   if (playerX==playerY):
     shoot=1
   else:
     shoot=0
   

  elif (playerX<enemyX):
      move = 'right'
      if (playerX==playerY):
          shoot=1
      else:
        shoot=0
  return move, shoot

#H-7summer
def h7summer(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
 
  if (bulletX==playerX) and (bulletY-playerY < 50):
      if (playerX < enemyX):
        move = 'right'
        shoot=None
        return move, shoot
      elif (playerX > enemyX):
        move = 'left'
        shoot=None
        return move, shoot
      else:
        shoot = True
        move='none'
        return move, shoot

  if (playerX < enemyX):
    move = 'right'
    shoot=None
    return move, shoot
  elif (playerX > enemyX):
    move = 'left'
    shoot=None
    return move, shoot
  else:
    shoot = True
    move='none'
    return move, shoot
  
#cosmic commandos
def cosmiccommandos(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  playerX=300
  directions = ['left', 'right']
  if enemyX< playerX or playerX==550:
    move = directions[0]
  elif enemyX>playerX or playerX==50:
    move = directions[1]
  else:
    i = random.randrange(0, 2)
    move = directions[i]
  if playerX-enemyX<=200:
    shoot = random.randrange(0,10)
    if shoot<5:
      shoot=True
    else:
      shoot=False
  return move, shoot

