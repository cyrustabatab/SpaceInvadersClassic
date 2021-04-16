import pygame,sys,os
from abc import ABC,abstractmethod
import math
import time
pygame.init()

SCREEN_WIDTH = SCREEN_HEIGHT = 800
screen  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
from boss import Boss
from spritesheet import Spritesheet

vec = pygame.math.Vector2



clock = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)


filename = os.path.join('assets','turret_sheet.png')
spritesheet = Spritesheet(filename)

turret_image = spritesheet.load_strip(pygame.Rect(0,0,96,96),1)[0]

turret_image = pygame.transform.rotate(turret_image,180)




class Bullet(pygame.sprite.Sprite):
    
    image = pygame.transform.scale(pygame.image.load(os.path.join('assets','m3.png')).convert_alpha(),(40,40))
    def __init__(self,x,y,vel,degrees):
        super().__init__()

        self.rect = self.image.get_rect(center=(x,y))
        
        self.vel = vel * 2
        self.pos = vec(self.rect.centerx,self.rect.centery)
        print(degrees,self.vel)


    def update(self):


        self.pos+= self.vel
        self.rect.center = self.pos




class Turret(pygame.sprite.Sprite):

    image = turret_image

    def __init__(self,left=True):
        super().__init__()

        
        if left:
            x = self.image.get_width()//2
        else:
            x = SCREEN_WIDTH - self.image.get_width()//2
        y = SCREEN_HEIGHT//2
        self.rect = self.image.get_rect(center=(x,y))
        self.left = left
        self.degree = 0 
        self.original_image = self.image


    def update(self,player):


        delta_y  = self.rect.centery - player.rect.centery
        delta_x = self.rect.centerx - player.rect.centerx

        angle = math.atan(delta_x/delta_y)

        degrees = angle  * (180/math.pi)
        
        self.current_target = degrees
        if degrees > 0:
            self.direction = -2
            self.degree += self.direction
            self.degree= max(self.current_target,self.degree)
        else:
            self.direction = 2
            self.degree += self.direction
            self.degree = min(self.current_target,self.degree)
        

        self.image = pygame.transform.rotate(self.original_image,self.degree)
        '''
        if self.left:
            if self.ship.rect.center < SCREEN_WIDTH//2: # left side
                pass
        else:
            if self.ship.rect.center >= SCREEN_WIDTH//2:
                pass
        '''


        






class Ship(pygame.sprite.Sprite,ABC):
    


    def __init__(self,x,y):
        super().__init__()
        self.rect = self.image.get_rect(center=(x,y))
    
    def draw(self,screen):
        screen.blit(self.image,self.rect)

    @abstractmethod
    def update(self):
        pass

class EnemyShip(Ship):

    image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets','cool_ship.png')).convert_alpha(),(100,100)),180)
    def __init__(self,x,y):
        super().__init__(x,y)
        
        self.original_image = self.image.copy()
        self.direction = 0


        self.original_position = vec(0,1)
        self.position = self.original_position

        self.degree = 0
        self.current_target = 0
        self.bullets = pygame.sprite.Group()
        self.start_time = time.time()
    

    def fire_bullet(self):

        bullet = Bullet(*self.rect.center,self.position,-self.degree)
        self.bullets.add(bullet)


    
    def draw(self,screen):
        super().draw(screen)
        self.bullets.draw(screen)



    def update(self,player):
        
        current_time = time.time()

        delta_y  = self.rect.centery - player.rect.centery
        delta_x = self.rect.centerx - player.rect.centerx

        angle = math.atan(delta_x/delta_y)

        degrees = angle  * (180/math.pi)
        
        self.current_target = degrees
        if degrees > 0:
            self.direction = -2
            self.degree += self.direction
            self.degree= max(self.current_target,self.degree)
        else:
            self.direction = 2
            self.degree += self.direction
            self.degree = min(self.current_target,self.degree)



        

        



        self.image = pygame.transform.rotate(self.original_image,self.degree)
        self.rect = self.image.get_rect(center=self.rect.center)

        self.position = self.original_position.rotate(-self.degree) 

        if current_time - self.start_time >= 1:
            self.fire_bullet()
            self.start_time = current_time
        

        self.bullets.update()

class PlayerShip(Ship):
    image = pygame.image.load(os.path.join('assets','spaceship.png')).convert_alpha()

    def __init__(self,x,y):
        super().__init__(x,y)

        self.speed = vec(0,0)
    

    def update(self):


        self.rect.center += self.speed





enemy = EnemyShip(400,300)

ship = PlayerShip(400,760)


ships = pygame.sprite.Group()

ships.add(enemy)
ships.add(ship)


turrets = pygame.sprite.Group()

left_turret = Turret()
right_turret = Turret(left=False)

turrets.add(left_turret)
turrets.add(right_turret)

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.speed.x -= 4
            elif event.key == pygame.K_RIGHT:
                ship.speed.x += 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.speed.x += 4
            elif event.key == pygame.K_RIGHT:
                ship.speed.x -= 4
    
    
    ship.update() 
    enemy.update(ship)


    if ship.rect.centerx < SCREEN_WIDTH//2:
        left_turret.update(ship)
    else:
        right_turret.update(ship)



    
    screen.fill(WHITE)

    ship.draw(screen)
    enemy.draw(screen)
    turrets.draw(screen)

    pygame.display.update()

    clock.tick(FPS)







