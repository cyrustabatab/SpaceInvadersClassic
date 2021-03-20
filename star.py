from item import Item
import os


class Star(Item):
    


    
    @property
    def image_path(self):
        return os.path.join('assets','star.png')
    

    def powerup(self,player):
        player.double_speed()








