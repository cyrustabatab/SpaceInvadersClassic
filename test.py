import pygame,sys
pygame.init()

screen  = pygame.display.set_mode((800,800))
from boss import Boss

clock = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)


boss  = pygame.sprite.GroupSingle(Boss(800,800))
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    boss.update()
    screen.fill(WHITE)

    boss.sprite.draw(screen)
    pygame.display.update()

    clock.tick(FPS)







