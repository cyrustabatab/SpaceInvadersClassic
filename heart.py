import pygame,os
from item import Item

vec = pygame.math.Vector2


class Heart(Item):




    @property
    def image_path(self):
        return os.path.join('assets','heart.png')
    
    def powerup(self,player):
        player.add_ten_health()

