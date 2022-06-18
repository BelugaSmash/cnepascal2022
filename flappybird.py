import os
import pygame, sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

gy = 0
x, y, w, h = 100, 720 / 2, 50, 50
pipex, pipey, pipew, pipeh = 1280, random.randint(720 / 2 - 200, 720 / 2 + 200), 100, 200

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
        pipex = 1300
    pygame.draw.rect(screen, (0, 255, 0), [pipex - pipew / 2, pipeh - 720 / 2, pipew, pipeh])
    pygame.draw.rect(screen, (0, 255, 0), [pipex - pipew / 2, pipeh + 720 / 2, pipew, pipeh])
    pygame.draw.rect(screen, (0, 0, 255), [x - w / 2, y - h / 2, w, h])
    if collide(x - w / 2, y - h / 2, w, h, pipex - pipew / 2, pipeh - 720 / 2, pipew, pipeh) or\
        collide(x - w / 2, y - h / 2, w, h, pipex - pipew / 2, pipeh + 720 / 2, pipew, pipeh) or\
        y < 0 or y > 720:
        font1 = pygame.font.SysFont(None,100)
        txt = font1.render('Game Over!',True,(0, 0, 0))
        txt_rect = txt.get_rect(center = (1280 / 2, 720 / 2))
        screen.blit(txt, txt_rect)
        pygame.display.update()
        break
    pygame.display.update()

pygame.time.delay(2000)
sys.exit()