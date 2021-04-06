import pygame
import random

vec = pygame.math.Vector2

def resize(images,size):

    for i,image in enumerate(images):
        image = pygame.transform.scale(image,(size,size))
        images[i] = image





class EnemyObject(pygame.sprite.Sprite):
    '''generic enemy class to represent enemy objects that spawn periodically(created sepearte class for spaceships since they behave much differnetly'''


    def __init__(self,screen_width,screen_height,speed,damage):
        super().__init__()
        x,y = random.randint(0,screen_width - self.image.get_width()),random.randint(-60,-40)
        
        self.screen_height = screen_height
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel = vec(0,speed)
        self.damage = damage


    def update(self):


        self.rect.center += self.vel


        if self.rect.top >= self.screen_height:
            self.kill()











