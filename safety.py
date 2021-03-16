from item import Item
import os



class Safety(Item):
    
    image_path = os.path.join('assets','x.png')
    def __init__(self,screen_width,screen_height,size=40):
        super().__init__(self.image_path,screen_width,screen_height,size)


    def powerup(self,player):


        player.add_five_hit_protection()



