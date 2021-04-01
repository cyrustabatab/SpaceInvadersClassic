import pygame

from item import Item
import os


def get_coin_images(size):

    directory = os.path.join('assets','gold_coin_animation')

    images = []
    for file_ in os.listdir(directory):

        image = pygame.transform.scale(pygame.image.load(os.path.join(directory,file_)).convert_alpha(),(size,size))
        images.append(image)
    

    return images









class Coin(Item):
    
    def __init__(self,screen_width,screen_height,size=40,speed=2):
        self.coin_images = get_coin_images(size)
        super().__init__(screen_width,screen_height,-1,speed)

        self.coin_image_index = 0
        self.frame_count = 0
        self.frame_limit = 4
    

    @property
    def image_path(self):
        return os.path.join('assets','gold_coin_animation',"gold_coin_round_blank_1.png")

    
    def update(self):
        super().update()


        self.frame_count += 1
        if self.frame_count == self.frame_limit:
            self.frame_count = 0
            self.coin_image_index = (self.coin_image_index + 1) % len(self.coin_images)
            self.image = self.coin_images[self.coin_image_index]

    

    def powerup(self,player):
        player.increment_coins()












