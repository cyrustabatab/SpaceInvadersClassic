from item import Item


class PowerUp(Item):
    

    image_path = None

    def __init__(self,screen_width,screen_height):
        super().__init__(self.image_path,screen_width,screen_height)


