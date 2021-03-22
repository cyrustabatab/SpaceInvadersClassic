from item import Item
import os
from text_utility import text_wrap



class PoisonMuk(Item):

    

    @property
    def text(self):
        text = "CAUSES YOU TO LOSE 2 HP A SECOND FOR 5 SECONDS"
        width = 28
        return text_wrap(text,width,self.font)


    @property
    def image_path(self):
        return os.path.join('assets','muk.png')
    

    def powerup(self,player):
        player.poison()

