from item import Item
import os



class Snowflake(Item):

    

    @property
    def text(self):
        text = "FREEZES YOU FOR FIVE SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    @property
    def image_path(self):
        return os.path.join('assets','snowflake.png')
    


    def powerup(self,player):
        player.freeze()






