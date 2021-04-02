from item import Item
import os



class Safety(Item):
    
    #def __init__(self,screen_width,screen_height,size=40):
        #super().__init__(self.image_path,screen_width,screen_height,size)
    
    
    name = 'safety' 

    @property
    def text(self):
        text = "PROTECT FROM FIVE HITS"
        WHITE  = (255,255,255)
        return self.font.render(text,True,WHITE)
    

    @property
    def image_path(self):
        return os.path.join('assets','x.png')


    def powerup(self,player):

        player.add_five_hit_protection()



