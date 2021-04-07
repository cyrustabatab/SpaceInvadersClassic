from item import Item
import os


class FreeMovement(Item):

    name = "free"    
    time_last = 10

    @property
    def text(self):
        text = "ALLOW TURNING FOR 10 SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    


    @property
    def image_path(self):
        return os.path.join('assets','arrow.png')
    


    @staticmethod
    def powerup(player):
        player.allow_turning()
    
