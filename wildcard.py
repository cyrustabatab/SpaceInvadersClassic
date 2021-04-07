from item import Item
from red_button import RedButton
from strength import Strength
import random
import os
from safety import Safety



WHITE = (255,255,255)


class WildCard(Item):

    possibilities = [RedButton,Strength,Safety]
    name = "wildcard"
    time_last = 0
    _image_path = os.path.join('assets','question_mark.png')

    @property
    def text(self):
        text = "Random PowerUp"
        return self.font(text,True,WHITE)

    
    @property
    def image_path(self):
        return self._image_path


    def powerup(self,player):

        class_ = random.choice(WildCard.possibilities)
        self.name = class_.name
        self.time_last = class_.time_last
        self._image_path = class_.image_path

        player.powerup()



