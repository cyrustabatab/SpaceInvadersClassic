from item import Item
import os
import textwrap
import random
import time
from text_utility import text_wrap
import pygame
from explosion_animation import Explosion

vec = pygame.math.Vector2

class Bomb(pygame.sprite.Sprite):
    

    image = pygame.transform.scale(pygame.image.load(os.path.join('assets','bomb.png')).convert_alpha(),(40,40))
    tick_sound = pygame.mixer.Sound(os.path.join('assets','ticking.wav'))

    def __init__(self,x,y,target_y,speed=5,detonation_time=3,distance=100):
        '''x and y represent the center of the bomb'''
        super().__init__()
        

        target_y = int(target_y) 

        target_y = (target_y//speed) * speed
        
        self.rect = self.image.get_rect(center=(x,y))
        self.vel = vec(0,-speed)
        self.target_y = target_y
        self.start_detonation = None
        self.detonation_time = detonation_time
        self.distance = distance
    


    
    def explode(self,aliens,explosions):

        

        self.tick_sound.stop()
        center = vec(*self.rect.center)

        for alien in aliens:
            alien_center = vec(*alien.rect.center)

            if center.distance_to(alien_center) <= self.distance:
                alien.kill()
                size = random.randint(1,3)
                explosions.add(Explosion(*alien.rect.center,size))

        

        size = 3
        explosions.add(Explosion(*self.rect.center,size))
        self.kill()



    

    def update(self,aliens,explosions):


        if  self.start_detonation:
            current_time = time.time()
            if current_time - self.start_detonation >= self.detonation_time:
                self.explode(aliens,explosions)



        else:
            self.rect.center += self.vel

            if self.rect.centery == self.target_y:
                self.vel.y = 0
                self.start_detonation = time.time()
                self.tick_sound.play()
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



