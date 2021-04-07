import pygame,os
from item import Item

vec = pygame.math.Vector2


class Heart(Item):


    name = 'heart'
    time_last = 0

    @property
    def image_path(self):
        return os.path.join('assets','heart.png')
    
    

    @property
    def text(self):
        text = "Adds 10 HP"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)

    @staticmethod
    def powerup(player):
        player.add_ten_health()

