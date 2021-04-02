from item import Item
import os
from text_utility import text_wrap



class Strength(Item):
    

    name = 'strength'

    @property
    def text(self):
        text = "DOUBLE YOUR DAMAGE FOR 10 SECONDS"
        width = 28
        WHITE = (255,255,255)
        return text_wrap(text,width,self.font)

    
    @property
    def time_last(self):
        return 10

    @property
    def image_path(self):
        return os.path.join('assets','strength.png')

    
    def powerup(self,player):

        player.increase_bullet_damage()

    @staticmethod
    def disable(player):    
        player.decrease_bullet_damage()


