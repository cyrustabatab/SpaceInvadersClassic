from item import Item
import os



class Strength(Item):
    

    name = 'strength'

    @property
    def text(self):
        text = "DOUBLE YOUR DAMAGE FOR 10 SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)

    
    @property
    def time_last(self):
        return 10

    @property
    def image_path(self):
        return os.path.join('assets','strength.png')

    
    def powerup(self,player):

        player.increase_bullet_damage()

    


