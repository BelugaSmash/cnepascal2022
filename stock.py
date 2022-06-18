import random
import pygame
import sys
import time

stock_num=[]
sample = 10000
stock_num_save = 0
global flag_first
flag_first=0
while 1:
    if flag_first==1:
        continue
    else:
        for i in range(0, 10):
            stock_num_save = random.randint(-100, 100)
            #time.sleep(1)
            stock_num.append(sample - stock_num_save)
            if i == 9:
                flag_first=1
                break
        print(stock_num)
    screen = pygame.display.set_mode((1280,720))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))