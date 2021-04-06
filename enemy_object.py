import pygame
import random
from abc import ABC
from explosion_animation import Explosion
vec = pygame.math.Vector2

def resize(images,size):

    for i,image in enumerate(images):
        image = pygame.transform.scale(image,(size,size))
        images[i] = image


GREEN = (0,255,0)
RED = (255,0,0)


class EnemyObject(pygame.sprite.Sprite,ABC):
    '''generic enemy class to represent enemy objects that spawn periodically(created sepearte class for spaceships since they behave much differnetly'''


    def __init__(self,screen_width,screen_height,speed,damage,hits):
        super().__init__()
        x,y = random.randint(0,screen_width - self.image.get_width()),random.randint(-60,-40)
        self.screen_height = screen_height
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel = vec(0,speed)
        self.damage = damage
        self.full_health = 100
        self.health = self.full_health
        self.full_hits = hits
        self.hits = hits

        
    def draw(self,screen):


        

        screen.blit(self.image,self.rect)
        if self.hits > 0:
            length =50
            pygame.draw.rect(screen,RED,(self.rect.centerx - length/2,self.rect.bottom,length,5))
            pygame.draw.rect(screen,GREEN,(self.rect.centerx - length/2,self.rect.bottom,(self.hits /self.full_hits) * (length),5))

    
    def take_a_hit(self,explosions):
        
        if self.hits > 0:
            self.hits -= 1
            if self.hits == 0:
                explosions.add(Explosion(*self.rect.center,size=3))
                self.kill()






    def update(self):


        self.rect.center += self.vel


        if self.rect.top >= self.screen_height:
            self.kill()











