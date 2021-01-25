import pygame
import sys
from pygame.locals import *
#初始化pygame
pygame.init()

size = width, height = 600, 400
speed = [-2, 1]
bg = (255,255,255)
#创建指定大小的窗口
screen = pygame.display.set_mode(size)
#窗口标题
pygame.display.set_caption("我是标题")
#加载图片
turtle = pygame.image.load("123.jpg")
#获得图像的位置矩形
position = turtle.get_rect()
l_head = turtle
r_head = pygame.transform.flip(turtle,True,False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                turtle = l_head
                speed = [-1,0]
            if event.key == K_RIGHT:
                turtle =r_head
                speed = [1,0]
            if event.key == K_UP:
                speed = [0,-1]
            if event.key == K_DOWN:
                speed = [0,1]
    #移动图像
    position = position.move(speed)
    if position.left<0 or position.right>width:
        #翻转图像
        turtle = pygame.transform.flip(turtle,True,False)
        #反方向移动
        speed[0] = -speed[0]
    if position.top<0 or position.bottom>height:
        speed[1] = -speed[1]
    #填充背景
    screen.fill(bg)
    #更新图像
    screen.blit(turtle,position)
    #更新界面
    pygame.display.flip()
    #延迟10毫秒
    pygame.time.delay(5)