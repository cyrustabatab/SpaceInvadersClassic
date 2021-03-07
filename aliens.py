import pygame,time,random
from alien import Alien



class Aliens:


    def __init__(self,screen_width,rows=5,columns=5):

        self.rows = rows
        self.columns = columns
        self.aliens = pygame.sprite.Group()
        
        self.top_gap = 50
        self.left_gap = 50
        self.gap = (screen_width - 100) / rows

        self.alien_cooldown = 2
        self._create_aliens()
        self.start_time = time.time()
        self.all_bullets = pygame.sprite.Group()
        

    def get_group(self):
        return self.aliens
    

    def get_bullets(self):
        return self.all_bullets

    def _create_aliens(self):

        for col in range(self.columns):
            for row in range(self.rows):
                alien = Alien(self.gap * col + self.gap/2,self.top_gap + 70* row + self.gap/2)
                self.aliens.add(alien)
        
        


    def draw(self,screen):

        self.aliens.draw(screen) 
        self.all_bullets.draw(screen)

    def update(self):
        
        current_time = time.time()
        if current_time - self.start_time >= self.alien_cooldown:
            aliens = random.sample(self.aliens.sprites(),3)
            for alien in aliens:
                bullet = alien.fire_bullet()
                self.all_bullets.add(bullet)

            self.start_time = current_time

        self.aliens.update()
        self.all_bullets.update()





