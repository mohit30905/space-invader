import random
def run(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
     # TODO THE LOGIC PART
     # bulletDist = abs(bulletY - playerY)
     # if bulletDist < 100:
     if bulletX - playerX  < 100:
          return 'right', True
     elif playerX - bulletX < 100 :
          return 'left', True
    
     if enemyX - playerX < 0:
        return 'right', True

     return 'left', True