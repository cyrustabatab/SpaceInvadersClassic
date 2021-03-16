from item import Item
import os


class Bomb(Item):


    @property
    def image_path(self):
        return os.path.join('assets','bomb.png')
    

    def powerup(self,player):
        pass
