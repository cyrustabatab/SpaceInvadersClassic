import pygame,os,random
from item import Item



class InvincibilityPotion(Item):


    name = 'potion'    
    time_last = 10

    @property
    def image_path(self):
        return os.path.join('assets','potion.png')
    

    @property
    def text(self):
        text = "PREVENT DAMAGE FOR 10 SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    

    @staticmethod
    def powerup(player):
        player.make_invincible()
    

    @staticmethod
    def disable(player):
        player.unprotect()








