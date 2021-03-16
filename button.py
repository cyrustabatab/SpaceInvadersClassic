import pygame,os



class Button(pygame.sprite.Sprite):
    
    font_path = os.path.join('assets','atari.ttf')
    
    def __init__(self,text,x,y,text_color,bg_color,callback,size=20):
        '''x and y represent center of button'''
        super().__init__()
        font = pygame.font.Font(self.font_path,size)
        
        self.bg_color = bg_color

        self.button_text = font.render(text,True,text_color)


        self.image = pygame.Surface((self.button_text.get_width() + 50,self.button_text.get_height() + 50),pygame.SRCALPHA)


        self.button_text_rect = self.button_text.get_rect(center=(self.image.get_width()//2,self.image.get_height()//2))

        self.image.fill(bg_color)


        self.alpha_color = (*bg_color,128)

        self.image.blit(self.button_text,self.button_text_rect)

        self.rect = self.image.get_rect(center=(x,y))
        self.callback = callback
        self.hovered_on = False

    

    def clicked_on(self,point):

        return self.rect.collidepoint(point)

    def update(self,point):
        
        collided = self.rect.collidepoint(point)

        if self.hovered_on and not collided:
            self.image.fill(self.bg_color)
            self.image.blit(self.button_text,self.button_text_rect)
            self.hovered_on = False
        elif not self.hovered_on and collided:
            self.image.fill(self.alpha_color)
            self.image.blit(self.button_text,self.button_text_rect)
            self.hovered_on = True




    


















