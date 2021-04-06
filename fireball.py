# fireball
from meteor import Meteor
from spritesheet import Spritesheet
import os

def get_fireball_images():
    path = os.path.join('assets','fire1_64.png')


    rows,cols = 6,10

    sheet = Spritesheet(path)

    images = []
    width = height = 64
    for row in range(rows):


        images.extend(sheet.load_strip((0,row * height,width,height),cols))



    return images








class Fireball(Meteor):


    images = get_fireball_images()


    def __init__(self,width,height,speed=3,frame_switch=1,damage=20):
        self.image = self.images[0]
        super().__init__(width,height,speed,frame_switch,damage,hits=-1)


















