from item import Item
from powerup import PowerUp
import os


class Skull(Item):
    


    @property
    def image_path(self):
        return os.path.join('assets','skull.png')


    def powerup(self,player):

        player.instant_die()

