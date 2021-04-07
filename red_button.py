from item import Item
import os

class RedButton(Item):


    
    name = 'red'
    time_last = 0

    @property
    def text(self):
        text = "CLEAR ALL ENEMY BULLETS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)
    


    @property
    def image_path(self):
        return os.path.join('assets','red_button.png')


    
    def powerup(self,player):
        super().powerup()
        return 'clear'






