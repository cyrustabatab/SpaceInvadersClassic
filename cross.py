import pygame,os,random
from item import Item




class Cross(Item):


    

    @property
    def image_path(self):
        return os.path.join('assets','cross.png') 
    
    def powerup(self,player):    
        player.set_full_health()









