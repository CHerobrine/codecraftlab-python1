import pygame
from pygame.locals import *
import random
score=0

class player(pygame.sprite.Sprite):
##    def __init__(self):
##        super(player,self).__init__()
##        self.surf=pygame.Surface((75,75))
##        self.surf.fill((255,0,0))
##        self.rect=self.surf.get_rect()
        
    def __init__(self):
        super(player, self).__init__()
        self.image=pygame.image.load("turtle.png").convert()
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect()
        self.rect.top=200
        self.rect.left=300
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
      #  if pressed_keys[K_LEFT]:
       #     self.rect.move_ip(-1,0)
       # if pressed_keys[K_RIGHT]:
      #      self.rect.move_ip(1,0)

        if self.rect.left<0:
            self.rect.left=0
        elif self.rect.right>800:
            self.rect.right = 800
        if self.rect.top<=0:
            self.rect.top=0
        elif self.rect.bottom>=600:
            self.rect.bottom=600

class opponent(pygame.sprite.Sprite):
    #def __init__(self):
      #  super(opponent,self).__init__()
       # self.surf=pygame.Surface((20,10))
      # self.surf.fill((0,255,0))
       # self.rect=self.surf.get_rect(center=(820,random.randint(0,600)))
       # self.speed=random.randint(0,2)
    def __init__(self):
        super(opponent,self).__init__()
        self.image=pygame.image.load('Person.png')
        self.image.set_colorkey((255,255,255),RLEACCEL)
        self.rect=self.image.get_rect(
            center=(random.randint(820,900),random.randint(0,600))
            )
        
        self.speed=random.randint(5,6)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        
   
        
        

        

        

pygame.init()
myfont=pygame.font.SysFont('helvetica',99
                           )
screen=pygame.display.set_mode((800,600))
player = player()
background=pygame.Surface(screen.get_size())
background.fill((0,122,224))

players=pygame.sprite.Group

opponents=pygame.sprite.Group()

all_sprites=pygame.sprite.Group()
all_sprites.add(player)
ADDOPPONENT=pygame.USEREVENT+1
pygame.time.set_timer(ADDOPPONENT,250)
#surf=pygame.Surface((75,75))
#surf.fill((200,0,1))
#rect=surf.get_rect()
running = True
clock=pygame.time.Clock()
fps=1000
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running=False
        elif event.type==QUIT:
            running=False
        elif(event.type==ADDOPPONENT):
            new_opponent=opponent()
            opponents.add(new_opponent)
            all_sprites.add(new_opponent)
    screen.blit(background,(0,0))
    pressed_keys=pygame.key.get_pressed()
    player.update(pressed_keys)
    opponents.update()
    #screen.blit(surf,(400,250))
    #screen.blit(player.surf,(400,250))
    #screen.blit(player.surf,player.rect)
    scoretext=myfont.render('Explosions='+str(score),1,(0,0,0))
    screen.blit(scoretext,(5,10))
    
    for entity in all_sprites: 
         screen.blit(entity.image, entity.rect)
    spr = pygame.sprite.spritecollideany(player,opponents)
    if spr:
        spr.kill()
        score +=1
    pygame.display.flip()


pygame.quit()

