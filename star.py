from item import Item
import os


class Star(Item):
    
    name = 'star'
    time_last = 10
    
    @property
    def image_path(self):
        return os.path.join('assets','star.png')
    

    @property
    def text(self):
        text = "SPEED BOOST FOR 10 SECONDS"
        WHITE = (255,255,255)

        return self.font.render(text,True,WHITE)



    @staticmethod
    def powerup(player):
        player.double_speed(Star.time_last)


    @staticmethod
    def disable(player):
        player.restore_normal_speed()





