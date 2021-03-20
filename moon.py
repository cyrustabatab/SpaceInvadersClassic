import pygame,os



def load_moon_images():
    directory = os.path.join('assets','hjm-moon')
    
    moon_images = []
    for file_ in os.listdir(directory):
        moon_image = pygame.image.load(os.path.join(directory,file_)).convert_alpha()
        moon_images.append(moon_image)
    
    return moon_images




class Moon(pygame.sprite.Sprite):


    images = load_moon_images()


    def __init__(self,x,y):
        super().__init__()


        self.image = self.images[0]


        self.rect = self.image.get_rect(center=(x,y))


        self.image_index = 0

    

    def update(self):


        self.image_index = (self.image_index + 1) % len(self.images)
        self.image = self.images[self.image_index]













