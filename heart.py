import pygame,os
from item import Item

vec = pygame.math.Vector2


class Heart(Item):

    image_path = os.path.join('assets','heart.png')


    def __init__(self,screen_width,screen_height,size=20):
        super().__init__(self.image_path,screen_width,screen_height,20)


    
    def powerup(self,player):
        player.add_ten_health()

