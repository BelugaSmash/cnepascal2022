import random
import pygame
import sys
import time

stock_num=[]
sample = 10000
stock_num_save = 0

j = 0
while 1:
    for i in range(0, 10):
        stock_num_save = random.randint(-100, 100)
        time.sleep(1)
        stock_num.append(sample - stock_num_save)
        j +=1 
        if i >= 10:
            break
    print(stock_num)
    screen = pygame.display.set_mode((1280,720))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))