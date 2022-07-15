#인공지능을 적이아닌 도우미로 만들기(주가 상승하락보여주기 등등)

import random

#부족하지만 등락을 정하는 코드
#주사위처럼 6까지의 난수를 뽑고, 1 ~ 3이라면 상승을, 4 ~ 6이라면 하락을
updown = list(range(10))
for i in range(1,11):
    num = random.randint(1,6)
    if num >= 1 and num < 4:
        updown[i] = 1
    if num >= 4 and num < 7:
        updown[i] = 2 
    print(updown[i])
#후에는 그래프 그리기를 넣고 인공지능을 탑재 
