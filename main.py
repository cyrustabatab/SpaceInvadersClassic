import pygame,sys,os
pygame.init()

WIDTH,HEIGHT = 600,800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))

from spaceship import Spaceship
from aliens import Aliens

clock = pygame.time.Clock()
pygame.display.set_caption("SPACE INVADERS")






player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
aliens = Aliens(WIDTH)



def game():
    

    background_image = pygame.image.load(os.path.join('assets','bg.png'))
    topleft=(0,0)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pressed_keys = pygame.key.get_pressed()
        aliens.update()
        player_ship.update(pressed_keys,aliens.get_group(),aliens.get_bullets()) 
        screen.blit(background_image,topleft)
        aliens.draw(screen)
        player_ship.draw(screen)
        player_ship.sprite.draw_health_bar_and_bullets(screen)
    

        pygame.display.update()
        clock.tick(FPS)




if __name__ == "__main__":
    
    game()



