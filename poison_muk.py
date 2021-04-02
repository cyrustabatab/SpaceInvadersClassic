from item import Item
import os
from text_utility import text_wrap



class PoisonMuk(Item):

    name = "poison"    

    @property
    def text(self):
        text = "CAUSES YOU TO LOSE 2 HP A SECOND UNTIL YOU HAVE AT LEAST 5 COINS TO PRESS J TO UNPOISON."
        width = 28
        return text_wrap(text,width,self.font)

    @property
    def time_last(self):
        return -1

    @property
    def image_path(self):
        return os.path.join('assets','muk.png')

    def powerup(self,player):
        player.poison()

    @staticmethod
    def disable(player):
        player.unpoison()
