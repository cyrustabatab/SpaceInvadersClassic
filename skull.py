from item import Item
from powerup import PowerUp
import os


class Skull(Item):
    

    

    @property
    def text(self):
        text = "Instant Death"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    @property
    def image_path(self):
        return os.path.join('assets','skull.png')


    def powerup(self,player):

        player.instant_die()

