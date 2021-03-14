import pygame,os,random
from item import Item



class InvincibilityPotion(Item):

    image_path = os.path.join('assets','potion.png')


    def __init__(self,screen_width,screen_height,size=40):
        super().__init__(self.image_path,screen_width,screen_height,size)
        

    def powerup(self,player):
        player.make_invincible()
    










