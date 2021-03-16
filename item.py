import pygame
import random
from abc import ABC,abstractmethod,abstractproperty


vec = pygame.math.Vector2


class Item(pygame.sprite.Sprite,ABC):
    
    

    def __init__(self,screen_width,screen_height,size=40,speed=2,rotate=0):
        super().__init__()
        

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))
        if rotate:
            self.image = pygame.transform.rotate(self.image,rotate)


        x = random.randint(0,screen_width - self.image.get_width())
        y = random.randint(-self.image.get_height() * 2,-self.image.get_height())


        self.screen_height = screen_height

        self.rect = self.image.get_rect(topleft=(x,y))

        self.vel = vec(0,speed)
    

    @abstractproperty
    def image_path(self):
        return None
    
    def update(self):

        self.rect.topleft += self.vel

        if self.rect.top > self.screen_height:
            self.kill()
    
    

    @abstractmethod
    def powerup(self,player):
        pass
