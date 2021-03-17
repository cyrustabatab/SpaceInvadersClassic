from item import Item
import os



class Snowflake(Item):


    @property
    def image_path(self):
        return os.path.join('assets','snowflake.png')
    


    def powerup(self,player):
        player.freeze()






