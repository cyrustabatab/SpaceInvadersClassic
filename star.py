from item import Item
import os


class Star(Item):
    


    
    @property
    def image_path(self):
        return os.path.join('assets','star.png')
    

    @property
    def text(self):
        text = "SPEED BOOST FOR 10 SECONDS"
        WHITE = (255,255,255)

        return self.font.render(text,True,WHITE)




    def powerup(self,player):
        player.double_speed()








