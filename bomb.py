from item import Item
import os
import textwrap
from text_utility import text_wrap
import pygame

vec = pygame.math.Vector2

class Bomb(pygame.sprite.Sprite):
    

    image = pygame.transform.scale(pygame.image.load(os.path.join('assets','bomb.png')).convert_alpha(),(40,40))

    def __init__(self,x,y,target_y,speed=5):
        '''x and y represent the center of the bomb'''
        super().__init__()
        

        target_y = int(target_y) 

        target_y = (target_y//speed) * speed
        
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0,-speed)
        self.target_y = target_y

    

    def update(self):
        self.rect.center += self.vel

        if self.rect.centery == self.target_y:
            self.vel.y = 0
        elif self.rect.top < 0:
            self.kill()








class BombPowerUp(Item):

    

    @property
    def text(self):
        text = "WEAPON THAT KILLS ENEMIES IN VICINITY WHEN DETONATED. HOLD DOWN ENTER AND RELEASE TO FLING BOMB. THE DISTANCE THE BOMB TRAVELS WILL DEPEND HOW LONG YOU HELD THE ENTER KEY."


        WHITE = (255,255,255)
        return text_wrap(text,28,self.font)

    @property
    def image_path(self):
        return os.path.join('assets','bomb.png')
    

    def powerup(self,player):
        player.add_bomb()



