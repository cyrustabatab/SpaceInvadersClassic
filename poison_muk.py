from item import Item
import os



class PoisonMuk(Item):

    

    @property
    def image_path(self):
        return os.path.join('assets','muk.png')


    def powerup(self,player):
        player.poison()

