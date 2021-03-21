import pygame,os
from item import Item

vec = pygame.math.Vector2


class Heart(Item):




    @property
    def image_path(self):
        return os.path.join('assets','heart.png')
    
    

    @property
    def text(self):
        text = "Adds 10 HP"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)

    def powerup(self,player):
        player.add_ten_health()

