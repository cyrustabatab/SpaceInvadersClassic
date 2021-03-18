from item import Item
import os


class FreeMovement(Item):


    @property
    def image_path(self):
        return os.path.join('assets','arrow.png')
    


    def powerup(self,player):
        player.allow_turning()

