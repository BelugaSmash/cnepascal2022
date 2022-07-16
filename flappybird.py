from distutils.command.build_scripts import first_line_re
import pygame, sys
import os
import random

#파이게임 초기화
pygame.init()
#파이게임 화면 크기 설정
screen = pygame.display.set_mode((1280, 720))

#변수들 초기화
cpath = os.path.dirname(__file__)
gy = 0
x, y, w, h = 100, 720 / 2, 50, 50
pipex, pipey, pipew, pipeh = [1280,  1280 + 1280 // 3, 1280 + 1280 * 2 // 3],\
     [random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100)], 100, 550
score = 0
font1 = pygame.font.SysFont(None,30)
game_over = False
first_game_over = True
change_score = 5
player_img = pygame.image.load(os.path.join(cpath, "pingu.png"))
game_over_img = pygame.image.load(os.path.join(cpath, "gameover.png"))
pipe_img = pygame.image.load(os.path.join(cpath, "pipe.png"))
pipe1_img = pygame.image.load(os.path.join(cpath, "pipe1.png"))

#게임 다시시작할 때 변수들 초기화
def game_restart():
    global gy, x, y, w, h, pipex, pipey, pipew, pipeh, score, game_over, first_game_over
    gy = 0
    x, y, w, h = 100, 720 / 2, 50, 50
    pipex, pipey, pipew, pipeh = [1280,  1280 + 1280 // 3, 1280 + 1280 * 2 // 3],\
        [random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100)], 100, 550
    score = 0
    game_over = False
    first_game_over = True

    mySound.stop()
    mySound2.stop()


#좌표, 가로 크기, 세로 크기가 주어졌을 때 충돌 했는지 체크
def collide(x, y, w, h, x_, y_, w_, h_):
    return x < x_ + w_ and y < y_ + h_ and x + w > x_ and y + h > y_

#그 뭐시기 그 그 그 FPS 그거 할려고 설정 할려고
clock = pygame.time.Clock()

while 1:
    #FPS를 60으로 설정
    clock.tick(60)
    #파이게임 기본 코드 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        #키가 눌렸다면
        if event.type==pygame.KEYDOWN:
            #눌린 키가 스페이스라면 점프
            if event.key == pygame.K_SPACE:
                if not game_over:
                    gy = 10.5
                    mySound = pygame.mixer.Sound("juuuuuump.wav")
                    mySound.play()
                else:
                    game_restart()
    
    #배경색을 흰색으로 채우기
    back_color = (255,255,255)
    if score >= change_score:
        back_color = (0,0,0)
    screen.fill(back_color)

    if not game_over:
        #중력 설정
        gy -= 0.5
        #y값을 중력값에 따라 떨어지게
        y -= gy

    #플레이어 화면에 그리기
    player_color = (0, 0, 255)
    if score >= change_score:
        player_color = (255, 0, 0)
    
    pygame.draw.rect(screen, (0, 255, 0), [x - w / 2, y - h / 2, w, h])
    pygame.draw.rect(screen, back_color, [x - w / 2 + 5, y - h / 2 + 5, w - 10, h - 10])
    screen.blit(player_img, (x - 25, y - 25))
    postxt = font1.render('(' + str(x) + ',' + str(y)+')',True,(255, 51, 153))
    screen.blit(postxt, (x - 50, y - 50))
    pygame.draw.rect(screen, (255, 51, 153), [x-5, y-5, 10, 10])
    #배관 관련 코드
    for i in range(3):
        if not game_over:
            #배관 왼쪽으로 이동
            pipex[i] -= 5 + 5 * (score >= change_score)
        
        #배관이 왼쪽 화면 밖으로 나갔다면 점수 + 1 하고 화면 오른쪽으로 보내기
        if pipex[i] <= 0 - pipew:
            pipex[i] = 1280 + pipew
            pipey[i] = random.randint(720/2, 720/2 + 300)
            score += 1

        # 배관 그리기
        pipe_color = (0, 255, 0)
        if score >= change_score:
            pipe_color = (100, 30, 30)
        
        pygame.draw.rect(screen, pipe_color, [pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh])
        pygame.draw.rect(screen, back_color, [pipex[i] - pipew / 2 + 5, pipey[i] - 720 / 2 - 345, pipew - 10, pipeh - 10])
        pygame.draw.rect(screen, pipe_color, [pipex[i] - pipew / 2, pipey[i] + 50, pipew, pipeh])
        pygame.draw.rect(screen, back_color, [pipex[i] - pipew / 2 + 5, pipey[i] + 55, pipew - 10, pipeh - 10])
        screen.blit(pipe_img, (pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350))
        screen.blit(pipe1_img, (pipex[i] - pipew / 2, pipey[i] + 50))
        postxt = font1.render('(' + str(pipex[i]) + ',' + str(pipey[i])+')',True,(255, 51, 153))
        screen.blit(postxt, (pipex[i] - 40, pipey[i] - 30))
        pygame.draw.rect(screen, (255, 51, 153), [pipex[i]-5, pipey[i]-5, 10, 10])
        #충돌했다면 게임 오버를 True로 설정
        if collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh) or\
            collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] + 50, pipew, pipeh) or\
            y < 0 or y > 720:
            game_over = True
    
    #점수 표시
    score_color = (0, 0, 0)
    if score >= change_score:
        score_color = (255,255,255)
    scoretxt = font1.render('score: ' + str(score),True,score_color)
    screen.blit(scoretxt, (10, 10))
    
    #게임 오버가 True라면 화면 가운데에 Game Over!표시 하고 게임을 정지 한다.
    if game_over:
        screen.blit(game_over_img, (0, 0))

        if first_game_over :
            mySound2 = pygame.mixer.Sound("121Nootnoot.wav")
            mySound2.play()
            first_game_over = False

    pygame.display.update()

#2초 기다리고 게임을 끈다.
pygame.time.delay(2000)
sys.exit()
