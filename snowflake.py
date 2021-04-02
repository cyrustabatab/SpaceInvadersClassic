from item import Item
import os



class Snowflake(Item):

    name = 'snowflake'

    @property
    def text(self):
        text = "FREEZES YOU FOR FIVE SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)

    @property
    def image_path(self):
        return os.path.join('assets','snowflake.png')
    
    

    @property
    def time_last(self):
        return 5


    def powerup(self,player):
        player.freeze()

    
    @staticmethod
    def disable(player):
        player.unfreeze()
    




