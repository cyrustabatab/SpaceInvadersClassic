import pygame,os,random
from item import Item




class Cross(Item):


    name = 'cross'    

    @property
    def image_path(self):
        return os.path.join('assets','cross.png') 
    

    @property
    def time_last(self):
        return 0


    @property
    def text(self):
        text = "RESTORE FULL HEALTH"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)

    def powerup(self,player):    
        player.set_full_health()









