from resources import fb_ai as ai
import pygame
import sys
import os
import random

# 파이게임 초기화
pygame.init()

# 창 제목 설정
pygame.display.set_caption("Pingu's Adventure")

# 파이게임 화면 크기 설정
screen = pygame.display.set_mode((1280, 720))

# 변수들 초기화
cpath = os.path.dirname(__file__)
gy = 0
x, y, w, h = 100, 720 / 2, 50, 50
pipex, pipey, pipew, pipeh = [1280, 1280 + 1280 // 3, 1280 + 1280 * 2 // 3], \
                             [random.randint(720 / 2, 720 / 2 + 100), random.randint(720 / 2, 720 / 2 + 100),
                              random.randint(720 / 2, 720 / 2 + 100)], 50, 500
pipe_img_w, pipe_img_h = 100, 550
score = 0
font1 = pygame.font.SysFont('Sans', 30)
font2 = pygame.font.SysFont('Sans', 50)
game_over = False
first_game_over = True
first_changed = False
ai_mode = False
change_score = 32
player_img = pygame.image.load("resources/pingu2.png")
game_over_img = pygame.image.load("resources/gameover.png")
pipe_img = pygame.image.load("resources/pipe.png")
pipe1_img = pygame.image.load("resources/pipe1.png")
tree_img = pygame.image.load("resources/tree.png")
tree1_img = pygame.image.load("resources/tree1.png")
title_img = [pygame.image.load("resources/title.png"),
             pygame.image.load("resources/title2.png"),
             pygame.image.load("resources/title3.png")]
setting_img = pygame.image.load("resources/setting.png")
level_img = [pygame.image.load("resources/easy_button.png"),
             pygame.image.load("resources/normal_button.png"),
             pygame.image.load("resources/hard_button.png")]
checkbox = [pygame.image.load("resources/checkbox.png"),
            pygame.image.load("resources/checkbox2.png")]
back_img = pygame.image.load("resources/back.png")
gamestart_img = [pygame.image.load("resources/gamestart.png"),
                 pygame.image.load("resources/gamestart1.png"),
                 pygame.image.load("resources/gamestart2.png")]
background_img = [pygame.image.load("resources/background.png").convert(),
                  pygame.image.load("resources/nam.png").convert(),
                  pygame.image.load("resources/background_pixel.png").convert()]
mawang_background_img = [pygame.image.load("resources/background_mawang.png").convert(),
                         pygame.image.load("resources/ma.png").convert(),
                         pygame.image.load("resources/background_pixel_mawang.png").convert()]
'''
player_img = pygame.image.load(os.path.join(cpath, "resources/pingu2.png"))
game_over_img = pygame.image.load(os.path.join(cpath, "resources/gameover.png"))
pipe_img = pygame.image.load(os.path.join(cpath, "resources/pipe.png"))
pipe1_img = pygame.image.load(os.path.join(cpath, "resources/pipe1.png"))
tree_img = pygame.image.load(os.path.join(cpath, "resources/tree.png"))
tree1_img = pygame.image.load(os.path.join(cpath, "resources/tree1.png"))
title_img = [pygame.image.load(os.path.join(cpath, "resources/title.png")),
             pygame.image.load(os.path.join(cpath, "resources/title2.png")),
             pygame.image.load(os.path.join(cpath, "resources/title3.png"))]
setting_img = pygame.image.load(os.path.join(cpath, "resources/setting.png"))
checkbox = [pygame.image.load(os.path.join(cpath, "resources/checkbox.png")),
            pygame.image.load(os.path.join(cpath, "resources/checkbox2.png"))]
back_img = pygame.image.load(os.path.join(cpath, "resources/back.png"))
gamestart_img = [pygame.image.load(os.path.join(cpath, "resources/gamestart.png")),
                 pygame.image.load(os.path.join(cpath, "resources/gamestart1.png")),
                 pygame.image.load(os.path.join(cpath, "resources/gamestart2.png"))]
background_img = [pygame.image.load(os.path.join(cpath, "resources/background.png")).convert(),
                  pygame.image.load(os.path.join(cpath, "resources/nam.png")).convert(),
                  pygame.image.load(os.path.join(cpath, "resources/background_pixel.png")).convert()]
mawang_background_img = [pygame.image.load(os.path.join(cpath, "resources/background_mawang.png")).convert(),
                         pygame.image.load(os.path.join(cpath, "resources/ma.png")).convert(),
                         pygame.image.load(os.path.join(cpath, "resources/background_pixel_mawang.png")).convert()]
'''
background_setting = 0
high_score = [0, 0, 0]
pipe_base_speed = 7.5
pipe_increase_speed = 7.5
level = 0

main_scene = True
is_setting_mode = False
stop_in_ai_mode = False
mute = False
mySound = pygame.mixer.Sound("resources/juuuuuump.wav")
mySound2 = pygame.mixer.Sound("resources/121Nootnoot2.wav")
mySound3 = pygame.mixer.Sound("resources/e_mart.wav")

mySound.set_volume(0.25)

ai = [ai.AI(), ai.AI(), ai.AI()]

# 게임 다시시작할 때 변수들 초기화
def game_restart():
    global gy, x, y, w, h, pipex, pipey, pipew, pipeh, score, game_over, first_game_over, first_changed
    gy = 0
    x, y, w, h = 100, 720 / 2, 50, 50
    # 파이프 x, y, 너비, 높이
    pipex, pipey, pipew, pipeh = [1280, 1280 + 1280 // 3, 1280 + 1280 * 2 // 3], \
                                 [random.randint(720 / 2, 720 / 2 + 100), random.randint(720 / 2, 720 / 2 + 100),
                                  random.randint(720 / 2, 720 / 2 + 100)], 50, 500
    score = 0
    game_over = False
    first_changed = False
    first_game_over = True
    mySound2.stop()


# 좌표, 가로 크기, 세로 크기가 주어졌을 때 충돌 했는지 체크
def collide(x, y, w, h, x_, y_, w_, h_):
    return x < x_ + w_ and y < y_ + h_ and x + w > x_ and y + h > y_


def dist(x1, x2):
    return abs(x1 - x2)


def get_nearest_pipe():
    li = [dist(pipex[0], x), dist(pipex[1], x), dist(pipex[2], x)]
    if min(li) == dist(pipex[0], x):
        return 0
    elif min(li) == dist(pipex[1], x):
        return 1
    return 2


# 그 뭐시기 그 그 그 FPS 그거 할려고 설정 할려고
clock = pygame.time.Clock()

main_scene_bgm = pygame.mixer.Sound('resources/nocturne.wav')
bgm = pygame.mixer.Sound('resources/stage_bgm.wav')
mawang_bgm = pygame.mixer.Sound("resources/mawang.wav")
bgm.set_volume(1.0)
main_scene_bgm.play(-1)

while 1:
    # FPS를 60으로 설정
    clock.tick(60)
    # 파이게임 기본 코드
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x_ = mouse_pos[0]
            y_ = mouse_pos[1]
            if is_setting_mode:
                if x_ >= 10 and x_ <= 110 and y_ >= 10 and y_ <= 110:
                    is_setting_mode = False
                elif x_ >= 800 and x_ <= 850 and y_ >= 150 and y_ <= 200:
                    ai_mode = not ai_mode
                elif x_ >= 800 and x_ <= 850 and y_ >= 500 and y_ <= 550:
                    mute = not mute
                    if mute:
                        main_scene_bgm.stop()
                    else:
                        main_scene_bgm.play(-1)
                elif x_ >= 750 and x_ <= 900 and y_ >= 225 and y_ <= 275:
                    level += 1
                    level %= 3
                else:
                    background_setting += 1
                    background_setting %= 3

            elif main_scene:
                # 설정 버튼 클릭했을때
                if x_ >= 1100 and x_ <= 1200 and y_ >= 600 and y_ <= 700:
                    is_setting_mode = True
                elif x_ >= 640 - 150 and x_ <= 640 + 150 and y_ >= 400 and y_ <= 500:
                    main_scene = False
                    main_scene_bgm.stop()
                    if not mute:
                        if level == 2:
                            mySound3.play()
                        else:
                            bgm.play()
            else:
                if not game_over and not ai_mode:
                    gy = 10
                    if not mute:
                        mySound.play()

        # 키가 눌렸다면
        if event.type == pygame.KEYDOWN:
            # 눌린 키가 스페이스라면 점프
            if event.key == pygame.K_SPACE:
                if main_scene and not is_setting_mode:
                    game_restart()
                    main_scene_bgm.stop()
                    if not mute:
                        if level == 2:
                            mySound3.play()
                        else:
                            bgm.play()
                    main_scene = False
                elif not is_setting_mode:
                    if not game_over:
                        if ai_mode:
                            stop_in_ai_mode = True
                            continue
                        gy = 10
                        if not mute:
                            mySound.play()
                    else:
                        game_restart()
                        main_scene = True
                        if not mute:
                            main_scene_bgm.play()

    if not main_scene:
        # 배경색을 흰색으로 채우기
        back_color = (255, 255, 255)
        if score >= change_score:
            screen.blit(mawang_background_img[background_setting], (0, 0))
            back_color = (0, 0, 0)
        else:
            screen.blit(background_img[background_setting], (0, 0))

        if score >= change_score:
            if not first_changed:
                first_changed = True
                bgm.stop()
                if not mute:
                    if level != 2:
                        mawang_bgm.play()

        if ai[level].jump(dist(pipex[get_nearest_pipe()], x), dist(pipey[get_nearest_pipe()], y)) and not game_over and ai_mode:
            gy = 10.5
            if not mute:
                mySound.play()

        if not game_over:
            # y값을 중력값에 따라 떨어지게
            y -= gy
            # 중력 설정
            gy -= 0.75 * (level + 1) / 3 * 2

        # 플레이어 화면에 그리기
        player_color = (0, 0, 255)
        if score >= change_score:
            player_color = (255, 0, 0)

        """
        pygame.draw.rect(screen, (0, 255, 0), [x - w / 2, y - h / 2, w, h])
        pygame.draw.rect(screen, back_color, [x - w / 2 + 5, y - h / 2 + 5, w - 10, h - 10])
        """

        screen.blit(player_img, (x - 25, y - 25))

        postxt = font1.render('(' + str(x) + ',' + str(y) + ')', True, (255, 51, 153))
        # screen.blit(postxt, (x - 50, y - 50))
        # pygame.draw.rect(screen, (255, 51, 153), [x-5, y-5, 10, 10])
        # 배관 관련 코드
        for i in range(3):
            if not game_over:
                # 배관 왼쪽으로 이동
                pipex[i] -= (pipe_base_speed + pipe_increase_speed * (score >= change_score)) * (level + 1) / 3 * 2

            # 배관이 왼쪽 화면 밖으로 나갔다면 점수 + 1 하고 화면 오른쪽으로 보내기
            if pipex[i] <= 0 - pipew:
                pipex[i] = 1280 + pipew
                pipey[i] = random.randint(720 / 2, 720 / 2 + 300)
                score += 1

            # 배관 그리기
            pipe_color = (0, 255, 0)
            if score >= change_score:
                pipe_color = (100, 30, 30)

            # 배관 히트박스 그리기
            """
            pygame.draw.rect(screen, pipe_color, [pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh])
            pygame.draw.rect(screen, back_color, [pipex[i] - pipew / 2 + 5, pipey[i] - 720 / 2 - 350 + 5, pipew - 10, pipeh - 10])
            pygame.draw.rect(screen, pipe_color, [pipex[i] - pipew / 2, pipey[i] + 100, pipew, pipeh])
            pygame.draw.rect(screen, back_color, [pipex[i] - pipew / 2 + 5, pipey[i] + 105, pipew - 10, pipeh - 10])
            """

            # 배관 그리기
            if score >= change_score:
                screen.blit(tree1_img, (pipex[i] - pipe_img_w / 2, pipey[i] - 720 / 2 - 350))
                screen.blit(tree_img, (pipex[i] - pipe_img_w / 2, pipey[i] + 50))
            else:
                screen.blit(pipe_img, (pipex[i] - pipe_img_w / 2, pipey[i] - 720 / 2 - 350))
                screen.blit(pipe1_img, (pipex[i] - pipe_img_w / 2, pipey[i] + 50))

            postxt = font1.render('(' + str(pipex[i]) + ',' + str(pipey[i]) + ')', True, (255, 51, 153))

            # screen.blit(postxt, (pipex[i] - 40, pipey[i] - 30))

            # 파이프 좌표 중심 그리기
            # pygame.draw.rect(screen, (255, 51, 153), [pipex[i]-5, pipey[i]-5, 10, 10])

            # 충돌했다면 게임 오버를 True로 설정
            if collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] - 720 / 2 - 350, pipew, pipeh) or \
                    collide(x - w / 2, y - h / 2, w, h, pipex[i] - pipew / 2, pipey[i] + 100, pipew, pipeh) or \
                    y < 0 or y > 720:
                game_over = True

        # 점수 표시
        score_color = (0, 0, 0)
        if score >= change_score:
            score_color = (255, 255, 255)
        scoretxt = font1.render('Score: ' + str(score), True, score_color)
        high_score[level] = max(high_score[level], score)
        screen.blit(scoretxt, (10, 10))
        highscoretxt = font1.render(f'High Score({"easy" if level == 0 else ("normal" if level == 1 else "hard")}): {high_score[level]}', True, score_color)
        screen.blit(highscoretxt, (10, 40))
        if ai_mode:
            gen_text = font1.render('Generation ' + str(
                ai[level].generation - (1 if not first_game_over and ai[level].current_ai == 0 else 0)) + ', ai' + str(
                (ai[level].current_ai - (1 if not first_game_over else 0)) % 50), True, score_color)
            screen.blit(gen_text, (10, 70))

        # 게임 오버가 True라면 화면 가운데에 Game Over!표시 하고 게임을 정지 한다.
        if game_over:
            screen.blit(game_over_img, (0, 0))
            if first_game_over:
                mawang_bgm.stop()
                bgm.stop()
                mySound3.stop()
                if not mute:
                    mySound2.play()
                first_game_over = False
                if ai_mode:
                    ai[level].game_over(score)
                    if not stop_in_ai_mode:
                        game_restart()
                        if not mute:
                            bgm.play()
                    else:
                        stop_in_ai_mode = False

    elif is_setting_mode:
        screen.blit(background_img[background_setting], (0, 0))
        txt = font1.render('Click To Change Background', True, (0, 0, 0))
        screen.blit(txt, (1280 / 2 - 150, 20))
        a_txt = font2.render('AI Mode', True, (0, 0, 0))
        a_pos = a_txt.get_rect(center=(1280/2, 175))
        screen.blit(a_txt, a_pos)
        level_txt = font2.render('Level', True, (0, 0, 0))
        level_pos = level_txt.get_rect(center=(1280/2, 250))
        screen.blit(level_txt, level_pos)
        mute_txt = font2.render('Mute', True, (0, 0, 0))
        mute_pos = mute_txt.get_rect(center=(1280/2, 525))
        screen.blit(mute_txt, mute_pos)
        screen.blit(checkbox[0 if not ai_mode else 1], (800,150))
        screen.blit(checkbox[0 if not mute else 1], (800,500))
        screen.blit(level_img[level], (800-50,225))
        screen.blit(back_img, (10, 10))
    else:
        screen.blit(background_img[background_setting], (0, 0))
        highscoretxt = font1.render(f'High Score({"easy" if level == 0 else ("normal" if level == 1 else "hard")}): {high_score[level]}', True, (0, 0, 0))
        screen.blit(highscoretxt, (10, 10))
        screen.blit(setting_img, (1100, 600))
        screen.blit(title_img[background_setting], (1280 / 2 - 320, 720 / 2 - 280))
        screen.blit(gamestart_img[background_setting], (1280 / 2 - 150, 400))

    pygame.display.update()

# 2초 기다리고 게임을 끈다.
pygame.time.delay(2000)
sys.exit()
