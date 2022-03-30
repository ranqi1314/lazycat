import pygame as p
import sys

p.init()
ziti = p.font.SysFont('华文楷体',50)
screen = p.display.set_mode((966,865))
p.display.set_caption('myself')
bg  = p.image.load('bg.png')
mu = p.mixer_music.load('bgm.mp3')
p.time.delay(1000)
p.mixer_music.play(-1)
with open('这个文件夹放你想说的话.txt', 'r', encoding='utf-8') as file:
    wen = file.read()
wen = wen.replace('\n','!')
wen_str = ''
wen_list = []
for i in wen:
    if i!='!':
        wen_str +=i
    else:
        wen_list.append(wen_str)
        wen_str = ''
xy = [(0,i*40) for i in range(len(wen_list)+1)]
ci ,geshu = 0,0
while True:
    if ci == len(wen_list):
        p.quit()
        sys.exit()
    temp = wen_list[ci]
    if temp[0:geshu] == temp:
        geshu = 0
        ci+=1
        p.time.delay(100)
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    if ci==5:
        wenzi = ziti.render('{}'.format(temp[0:geshu+1]),True,(255,0,0))
    else:
        wenzi = ziti.render('{}'.format(temp[0:geshu+1]),True,(0,0,0))
    geshu +=1
    p.time.delay(100)
    screen.blit(wenzi,xy[ci])
    p.display.update()