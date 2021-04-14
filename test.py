import pygame,sys,os
from abc import ABC,abstractmethod
import math
pygame.init()

screen  = pygame.display.set_mode((800,800))
from boss import Boss

vec = pygame.math.Vector2



clock = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)


class Ship(pygame.sprite.Sprite,ABC):
    


    def __init__(self,x,y):
        super().__init__()
        self.rect = self.image.get_rect(center=(x,y))
    
    def draw(self):
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

        self.degree = 0
        self.current_target = 0

    

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
        self.rect = self.image.get_rect(center=self.rect.center)


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



    
    screen.fill(WHITE)

    ships.draw(screen)

    pygame.display.update()

    clock.tick(FPS)







