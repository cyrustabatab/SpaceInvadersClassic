import pygame,os,random
from item import Item



class InvincibilityPotion(Item):


    

    @property
    def image_path(self):
        return os.path.join('assets','potion.png')

    def powerup(self,player):
        player.make_invincible()
    










