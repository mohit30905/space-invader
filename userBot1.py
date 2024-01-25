import random
from teamScripts import noname, cosmiccommandos, hecker, codemasters, crocin, teamrandom, starboss, helloworld, rocket, coderangers, h7summer 

def run(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
   directions = ['left', 'right','none']
  i = random.randint(0,1)
  move = directions[2]
  bulletCount = 20
  shoot = 0
  if bulletX == playerX:
    move = directions[i]
  else:
    move = directions[2]
    shoot=1
  while bulletCount<0:
    while True:
      if enemyX<playerX:
        move = directions[0]
      elif enemyX> playerX:
        move = directions[1]
      else:
        break
    if enemyX - playerX == 0: 
      shoot = 1
      move = directions[i]
    else:
      shoot = 0
    bulletCount = bulletCount - 1      
  return move , shoot
   # return noname(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount) #change team name here
