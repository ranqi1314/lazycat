import pygame as p
import sys

p.init()
ziti = p.font.SysFont('华文楷体',89)
screen = p.display.set_mode((966,865))
p.display.set_caption('myself')
bg_b  = p.image.load('bg_b.png')
bg_w  = p.image.load('bg_w.png')
mu = p.mixer_music.load('bgm.mp3')
p.time.delay(1000)
p.mixer_music.play(-1)
with open('这个文件夹放你想说的话2.txt', 'r', encoding='utf-8') as file:
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

ci,geshu,bg_num = 0,0,0
while True:
    temp = wen_list[ci]
    if temp == temp[0:geshu]:
        ci +=1
        geshu =0
    elif ci== len(wen_list):
        p.quit()
        sys.exit()
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    if bg_num%2<1:
        screen.blit(bg_b,(0,0))
        wenzi = ziti.render('{}'.format(temp[0:geshu+1]), True, (0, 0, 0))
    else:
        screen.blit(bg_w, (0, 0))
        wenzi = ziti.render('{}'.format(temp[0:geshu+1]), True, (255,255,255))
    geshu+=1
    bg_num +=1
    p.time.delay(150)
    screen.blit(wenzi,(99-30,355))
    p.display.update()