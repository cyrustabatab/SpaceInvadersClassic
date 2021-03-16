import pygame



class Text(pygame.sprite.Sprite):


    def __init__(self,text,x,y,font_path,font_size,text_color,bg_color=None,center_coordinate=False):
        super().__init__()


        font = pygame.font.Font(font_path,font_size)


        self.image = font.render(text,True,text_color,bg_color)

        
        if center_coordinate:
            self.rect = self.image.get_rect(center=(x,y))
        else:
            self.rect = self.image.get_rect(topleft=(x,y))

    

