import pygame, sys
import random

#파이게임 초기화
pygame.init()
#파이게임 화면 크기 설정
screen = pygame.display.set_mode((1280, 720))

#변수들 초기화
gy = 0
x, y, w, h = 100, 720 / 2, 50, 50
pipex, pipey, pipew, pipeh = [1280,  1280 + 1280 / 3, 1280 + 1280 * 2 / 3],\
     [random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100)], 100, 550
score = 0
font1 = pygame.font.SysFont(None,30)
game_over = False

#게임 다시시작할 때 변수들 초기화
def game_restart():
    gy = 0
    x, y, w, h = 100, 720 / 2, 50, 50
    pipex, pipey, pipew, pipeh = [1280,  1280 + 1280 / 3, 1280 + 1280 * 2 / 3],\
        [random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100),random.randint(720/2, 720/2 + 100)], 100, 550
    score = 0
    game_over = False


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
                else:
                    game_restart()
    
    #배경색을 흰색으로 채우기
    screen.fill((255,255,255))
    if not game_over:
        #중력 설정
        gy -= 0.5
        #y값을 중력값에 따라 떨어지게
        y -= gy
    
    #플레이어 화면에 그리기
    pygame.draw.rect(screen, (0, 0, 255), [x - w / 2, y - h / 2, w, h])
    #배관 관련 코드
    for i in range(3):
        if not game_over:
            #배관 왼쪽으로 이동
            pipex[i] -= 5
        
        #배관이 왼쪽 화면 밖으로 나갔다면 점수 + 1 하고 화면 오른쪽으로 보내기
        if pipex[i] <= 0 - pipew:
            pipex[i] = 1280 + pipew
            pipey[i] = random.randint(720/2, 720/2 + 300)
            score += 1

        # 배관 그리기
        pygame.draw.rect(screen, (0, 255, 0), [pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh])
        pygame.draw.rect(screen, (0, 255, 0), [pipex[i] - pipew / 2, pipey[i] + 50, pipew, pipeh])
        #충돌했다면 게임 오버를 True로 설정
        if collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh) or\
            collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] + 50, pipew, pipeh) or\
            y < 0 or y > 720:
            game_over = True
    
    #점수 표시
    scoretxt = font1.render('score: ' + str(score),True,(0, 0, 0))
    screen.blit(scoretxt, (10, 10))
    
    #게임 오버가 True라면 화면 가운데에 Game Over!표시 하고 게임을 정지 한다.
    if game_over:
        font2 = pygame.font.SysFont(None,100)
        txt = font2.render('Game Over!',True, (0, 0, 0))
        txt_rect = txt.get_rect(center = (1280 / 2, 720 / 2))
        screen.blit(txt, txt_rect)
        pygame.display.update()

    pygame.display.update()

#2초 기다리고 게임을 끈다.
pygame.time.delay(2000)
sys.exit()
