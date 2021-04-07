import pygame
import random
from abc import ABC,abstractmethod,abstractproperty,ABCMeta,abstractstaticmethod
import os
from copy import copy



vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite,ABC):
    
    
    font = pygame.font.Font(os.path.join('assets','atari.ttf'),20)
    time_last = -1
    question_mark_image = pygame.transform.scale(pygame.image.load(os.path.join('assets','question_mark.png')).convert_alpha(),(40,40))
    def __init__(self,screen_width,screen_height,size=40,speed=2,rotate=0,hidden=False):
        super().__init__()
        
        self.hidden = hidden
        self.image = pygame.image.load(self.image_path).convert_alpha()
        if size <= 0:
            size = self.image.get_width()
        if size > 0:
            self.image = pygame.transform.scale(self.image,(size,size))
        if rotate:
            self.image = pygame.transform.rotate(self.image,rotate)
         
        self.temp_image = self.image
        if self.hidden:
            self.image = self.question_mark_image

        self.big_image = pygame.transform.scale(self.image,(size + 15,size + 15))
        self.original_image = self.image.copy()

        x = random.randint(0,screen_width - self.image.get_width())
        y = random.randint(-self.image.get_height() * 2,-self.image.get_height())


        self.screen_height = screen_height

        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.big_rect = self.big_image.get_rect(center=self.rect.center)
        
        self.vel = vec(0,speed)
    

    def getImage(self):
        return self.temp_image

    @property
    def text(self):
        return None
    

    
    def change_rects_topleft(self,x,y):
        self.rect.topleft = x,y
        self.original_rect = self.rect.copy()
        self.big_rect = self.big_image.get_rect(center=self.rect.center)



    @abstractproperty
    def image_path(self):
        return None
    
    def update(self):

        self.rect.topleft += self.vel

        if self.rect.top > self.screen_height:
            self.kill()
    


    def is_hovered_on(self,point):
        if self.original_rect.collidepoint(point):
            self.image = self.big_image
            self.rect = self.big_rect
            return True
        self.image = self.original_image
        self.rect = self.original_rect
        return False



    @abstractmethod
    def powerup(self):
        if self.hidden:
            self.image = self.temp_image
            self.hidden = False

