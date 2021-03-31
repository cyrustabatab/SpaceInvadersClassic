from item import Item



class Strength(Item):

    @property
    def text(self):
        text = "DOUBLE YOUR DAMAGE FOR 10 SECONDS"
        WHITE = (255,255,255)
        return self.font.render(text,True,WHITE)


    @property
    def image_path(self):
        pass





