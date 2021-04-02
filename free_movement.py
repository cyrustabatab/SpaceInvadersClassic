from item import Item
import os


class FreeMovement(Item):

    name = "free"    

    @property
    def text(self):
        text = "ALLOW TURNING FOR 10 SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    

    @property
    def time_last(self):
        return 10

    @property
    def image_path(self):
        return os.path.join('assets','arrow.png')
    


    def powerup(self,player):
        player.allow_turning()
    
