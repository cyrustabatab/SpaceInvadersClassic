import pygame,sys,os,time
pygame.init()

WIDTH,HEIGHT = 600,800
FPS = 60
screen = pygame.display.set_mode((WIDTH,HEIGHT))

from spaceship import Spaceship
from aliens import Aliens

clock = pygame.time.Clock()
title = "SPACE INVADERS"
pygame.display.set_caption(title)




WHITE = (255,255,255)


background_image = pygame.image.load(os.path.join('assets','bg.png'))

def game():
    


    def reset():
        nonlocal player_ship,aliens,game_over,started,seconds,seconds_text,start_time,second_text_rect
        player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
        aliens = Aliens(WIDTH)
        started = False
        game_over = False
        seconds =3
        seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
        second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
        start_time = time.time()
        start_sound.play()
    font = pygame.font.SysFont('comicsansms',42)
    game_over_text = font.render("GAME OVER!",True,WHITE)
    gap_from_center = 50
    game_over_text_rect = game_over_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
    pygame.mixer.music.load(os.path.join('assets','level1.ogg'))

    start_sound = pygame.mixer.Sound(os.path.join('assets','racestart.wav'))

    player_ship = pygame.sprite.GroupSingle(Spaceship(WIDTH,HEIGHT))
    aliens = Aliens(WIDTH)

    explosions = pygame.sprite.Group()

    game_over = False
    topleft=(0,0)
    
    started = False

    start_time = time.time()
    seconds =3
    texts = ["READY!","SET!","GO!"]
    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
    start_sound.play()
    while True:
        

        if not started:
            current_time = time.time()
            if current_time - start_time >= 1:
                seconds -= 1
                if seconds == 0:
                    started = True
                    pygame.mixer.music.play(-1)
                else:
                    seconds_text = font.render(texts[len(texts) - seconds],True,WHITE)
                    second_text_rect =seconds_text.get_rect(center=(WIDTH//2,HEIGHT//2 + gap_from_center))
                    start_time = current_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                reset()

        
        explosions.update()
        if started and not game_over:
            pressed_keys = pygame.key.get_pressed()
            aliens.update()
            game_over = player_ship.sprite.update(pressed_keys,aliens.get_group(),aliens.get_bullets(),explosions) 
        screen.blit(background_image,topleft)
        aliens.draw(screen)
        player_ship.draw(screen)
        explosions.draw(screen)
        if  not game_over:
            player_ship.sprite.draw_health_bar_and_bullets(screen)

        if not started:
            screen.blit(seconds_text,second_text_rect)
            
        elif game_over:
            screen.blit(game_over_text,game_over_text_rect)
        

        pygame.display.update()
        clock.tick(FPS)


def menu():
    title_font = pygame.font.SysFont("comicsansms",50)
    top_gap = 50
    title_text = title_font.render("SPACE INVADERS",True,WHITE)

    title_text_rect= title_text.get_rect(center=(WIDTH//2,top_gap + title_text.get_height()//2))
    
    topleft = (0,0)
    pygame.mixer.music.load(os.path.join('assets','intro.ogg'))
    pygame.mixer.music.play(-1)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    game()



        
        screen.blit(background_image,topleft)

        screen.blit(title_text,title_text_rect)
        pygame.display.update()




if __name__ == "__main__":
    
    menu()



