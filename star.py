from item import Item
import os


class Star(Item):
    
    image_path = os.path.join('assets','star.png') 

    def __init__(self,screen_width,screen_height,size=40):
        super().__init__(self.image_path,screen_width,screen_height,size)


    

    def powerup(self,player):
        player.double_speed()








