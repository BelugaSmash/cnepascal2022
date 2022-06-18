import pygame, sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

gy = 0
x, y, w, h = 100, 720 / 2, 50, 50
pipex, pipey, pipew, pipeh = 1280, random.randint(720/2, 720/2 + 100), 100, 550
score = 0
font1 = pygame.font.SysFont(None,30)

def collide(x, y, w, h, x_, y_, w_, h_):
    return x < x_ + w_ and y < y_ + h_ and x + w > x_ and y + h > y_


clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gy = 10.5
    
    screen.fill((255,255,255))
    pipex -= 5
    gy -= 0.5
    y -= gy
    if pipex <= 0 - pipew:
        pipex = 1280 + pipew
        pipey = random.randint(720/2, 720/2 + 300)
        score += 10
    
    pygame.draw.rect(screen, (0, 255, 0), [pipex - pipew / 2, pipey - 720 / 2 - 350, pipew, pipeh])
    pygame.draw.rect(screen, (0, 255, 0), [pipex - pipew / 2, pipey + 50, pipew, pipeh])
    pygame.draw.rect(screen, (0, 0, 255), [x - w / 2, y - h / 2, w, h])
    scoretxt = font1.render('score: ' + str(score),True,(0, 0, 0))
    screen.blit(scoretxt, (10, 10))
    if collide(x - w / 2, y - h / 2, w, h, pipex - pipew / 2, pipey - 720 / 2 - 350, pipew, pipeh) or\
        collide(x - w / 2, y - h / 2, w, h, pipex - pipew / 2, pipey + 50, pipew, pipeh) or\
        y < 0 or y > 720:
        font2 = pygame.font.SysFont(None,100)
        txt = font2.render('Game Over!',True,(0, 0, 0))
        txt_rect = txt.get_rect(center = (1280 / 2, 720 / 2))
        screen.blit(txt, txt_rect)
        pygame.display.update()
        break
    pygame.display.update()

pygame.time.delay(2000)
sys.exit()